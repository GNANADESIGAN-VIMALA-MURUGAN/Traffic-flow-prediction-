# Traffic Flow Prediction App

A Flask-based web application for predicting traffic flow using AI and machine learning models.

## Features

- **User Authentication**: Register and login system
- **AI-Based Prediction**: Uses Groq API for real-time traffic predictions based on location
- **Data-Based Prediction**: Machine learning model for traffic volume prediction
- **Responsive UI**: Clean web interface for easy interaction

## Requirements

- Python >= 3.8

## Setup

1. **Clone the repository** (if applicable) and navigate to the project directory.

2. **Create a virtual environment**:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   - Copy `.env.example` to `.env`
   - Fill in your actual values:
     - Get a Groq API key from [Groq Console](https://console.groq.com/)
     - Generate a secure SECRET_KEY (you can use `python -c "import secrets; print(secrets.token_hex(32))"`)

5. **Run the application**:
   ```bash
   python app.py
   ```

6. **Access the app**:
   - Open your browser and go to `http://127.0.0.1:5000/`
   - The app will automatically open in your default browser.

## Usage

- **Register/Login**: Create an account or log in to access the features.
- **AI-Based Prediction**: Enter latitude and longitude to get traffic predictions using Groq AI.
- **Data-Based Prediction**: Input date, time, and junction number for ML-based predictions.

## Project Structure

- `app.py`: Main Flask application
- `traffic_model.pkl`: Pre-trained machine learning model
- `templates/`: HTML templates for the web interface
- `static/`: CSS and other static files
- `instance/users.db`: SQLite database for user data
- `requirements.txt`: Python dependencies

## Technologies Used

- **Backend**: Flask, SQLAlchemy, Flask-Login
- **AI**: Groq API (Llama 3.1 model)
- **ML**: Scikit-learn (for data-based predictions)
- **Frontend**: HTML, CSS
- **Database**: SQLite

## Notes

- Ensure your Groq API key has sufficient credits for usage.
- The machine learning model (`traffic_model.pkl`) should be in the same directory as `app.py`.
- The app runs in debug mode by default.