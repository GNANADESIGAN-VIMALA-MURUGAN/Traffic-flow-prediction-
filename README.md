# Traffic Flow Prediction

A web application for predicting traffic flow using both AI-based and data-driven approaches. This Flask-based app provides real-time traffic insights and historical data predictions to help users make informed decisions about travel routes and times.

## Features

- **User Authentication**: Secure login and registration system
- **AI-Based Prediction**: Real-time traffic information using Groq AI (Llama 3.1 model) based on location coordinates and current time
- **Data-Based Prediction**: Machine learning model predictions using historical traffic data for specific junctions and timestamps
- **Interactive Web Interface**: User-friendly templates for easy navigation and data input
- **Responsive Design**: Modern CSS styling for optimal viewing on various devices

## Technologies Used

- **Backend**: Flask (Python web framework)
- **Database**: SQLite with SQLAlchemy ORM
- **Authentication**: Flask-Login
- **AI Integration**: Groq API (OpenAI-compatible)
- **Machine Learning**: Scikit-learn, Pandas, NumPy
- **Frontend**: HTML, CSS, JavaScript
- **Model Storage**: Pickle for serialized ML models

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/GNANADESIGAN-VIMALA-MURUGAN/Traffic-flow-prediction-.git
   cd Traffic-flow-prediction-
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**:
   The application will automatically create the SQLite database when you run it for the first time.

5. **Configure API Key**:
   - Sign up for a Groq API account at [https://console.groq.com](https://console.groq.com)
   - Replace the `GROQ_API_KEY` in `app.py` with your actual API key

## Usage

1. **Run the application**:
   ```bash
   python app.py
   ```

2. **Access the web app**:
   Open your browser and navigate to `http://127.0.0.1:5000`

3. **Register/Login**:
   - Create an account or log in with existing credentials

4. **AI-Based Prediction**:
   - Navigate to the AI-based prediction page
   - Enter latitude and longitude coordinates
   - Get real-time traffic information powered by AI

5. **Data-Based Prediction**:
   - Go to the data-based prediction page
   - Select a junction number and date/time
   - Receive predicted traffic volume based on historical data

## Project Structure

```
traffic-flow-prediction/
│
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── traffic_model.pkl      # Trained machine learning model
├── README.md             # Project documentation
│
├── instance/
│   └── users.db          # SQLite database for user authentication
│
├── static/
│   └── styles.css        # CSS stylesheets
│
└── templates/
    ├── index.html        # Home page
    ├── login.html        # Login page
    ├── register.html     # Registration page
    ├── ai.html           # AI-based prediction interface
    └── data.html         # Data-based prediction interface
```

## API Endpoints

- `GET /` - Home page
- `GET /login` - Login page
- `POST /login` - Process login
- `GET /register` - Registration page
- `POST /register` - Process registration
- `GET /logout` - Logout
- `GET /ai-based-prediction` - AI prediction page
- `POST /get-traffic` - Get AI-based traffic data
- `GET /data-based-prediction` - Data prediction page
- `POST /predict-traffic` - Get ML-based traffic prediction

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Groq for providing the AI API
- Flask community for the excellent web framework
- Scikit-learn for machine learning tools