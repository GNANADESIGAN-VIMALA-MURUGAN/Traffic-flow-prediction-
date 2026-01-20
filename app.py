from openai import OpenAI
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
import datetime
import re
import pickle
import numpy as np
from flask import request
import pandas as pd
import webbrowser
import threading

# Initialize Flask App
app = Flask(__name__)

# Secret Key and Database Configuration
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

# Flask-Login Configuration
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Set up Groq AI API
GROQ_API_KEY = "https://console.groq.com/home"  # Your Groq API Key from Groq
client = OpenAI(api_key=GROQ_API_KEY, base_url="https://api.groq.com/openai/v1")

# User Model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Home Route
@app.route('/')
def home():
    return render_template('index.html', user=current_user)

# AI-Based Prediction Route
@app.route('/ai-based-prediction')
def ai_based_prediction():
    return render_template('ai.html')

# Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            login_user(user)
            return redirect(url_for('home'))
    return render_template('login.html')

# Register Route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

# Logout Route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# API Route for Traffic Prediction using Gemini AI
@app.route('/get-traffic', methods=['POST'])
def get_traffic():
    data = request.json
    lat = data.get('latitude')
    lon = data.get('longitude')

    if lat is None or lon is None:
        return jsonify({"error": "Invalid location data"}), 400

    # Get system time in 24-hour format
    current_time = datetime.datetime.now().strftime("%I:%M %p")

    # Construct prompt for Gemini AI
    prompt = f"""
    Provide live traffic flow details for the location at latitude {lat} and longitude {lon}.
    The current system time is {current_time}.
    Include information relevant to the time of day, expected congestion, and road conditions.
    Format the response with clear headings and bullet points for better readability. Don't say
    you are an AI model and all.. Even rough prediction would do. I am displaying this on my app. 
    So don't give any response that involves you telling you cannot do something. The response should
    be on point. Don't ask them to check in another app and all. Don't give disclaimers as well.
    """

    # Use Groq AI to get traffic data
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    traffic_info = response.choices[0].message.content if response.choices[0].message.content else "Traffic data unavailable"

    return jsonify({"traffic": format_traffic_response(traffic_info)})

def format_traffic_response(response_text):
    """
    Formats the AI response for proper rendering in HTML.
    - Converts markdown-style bold to proper HTML <b> tags.
    - Ensures bullet points render correctly.
    - Adds appropriate spacing and line breaks.
    - Removes unwanted stray asterisks (*).
    """

    # Convert bold text (**text**) to HTML bold (<b>text</b>)
    response_text = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", response_text)

    # Convert markdown bullet points (* item) into proper HTML list format
    response_text = response_text.replace("\n* ", "\n• ")  # Change * to • for bullets
    response_text = response_text.replace("\n", "<br>")  # Ensure line breaks are correctly rendered
    
    # Add spacing for readability
    response_text = response_text.replace("•", "<br>•")  # Add spacing for bullets
    response_text = response_text.replace("**", "")  # Remove any unconverted **

    return response_text

# Load the trained model
model_file = "traffic_model.pkl"
with open(model_file, "rb") as file:
    model = pickle.load(file)

@app.route('/data-based-prediction')
def data_based_prediction():
    return render_template('data.html')

@app.route('/predict-traffic', methods=['POST'])
def predict_traffic():
    try:
        # Get input values from the form
        date_time = request.form["datetime"]
        junction = int(request.form["junction"])

        # Convert DateTime input to timestamp
        timestamp = pd.to_datetime(date_time).timestamp()

        # Prepare input data for prediction
        input_data = np.array([[timestamp, junction]])

        # Predict traffic volume
        predicted_vehicles = model.predict(input_data)[0]

        return jsonify({"prediction": int(predicted_vehicles)})

    except Exception as e:
        return jsonify({"error": str(e)})


# Run the Flask App
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Ensures the database tables are created
    app.run(debug=True)
def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000/")

if __name__ == '__main__':
    if not hasattr(open_browser, "has_run"):  # Prevent multiple openings
        open_browser.has_run = True
        threading.Timer(1.5, open_browser).start()  # Delay for smooth opening
    app.run(debug=True, use_reloader=False)