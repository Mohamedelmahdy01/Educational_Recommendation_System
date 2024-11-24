# ML-Powered Educational Recommendation System

A Flask-based web application that uses a machine learning model to recommend the most suitable field in software development for students, based on their responses to a series of questions.

## Features

- Predicts the most suitable field (e.g., Front-End, Back-End, Data Science) based on user responses.
- API built with Flask for easy deployment and interaction.
- Pre-trained Random Forest model used for predictions.
- Balanced dataset to improve model accuracy.

## Dataset

The dataset contains responses to 20 questions designed to evaluate a user's interests and skills. The data is balanced to ensure accurate recommendations.

---

## Requirements

Make sure you have the following installed:

- Python 3.7+
- Flask
- Scikit-learn
- Pandas
- Pickle

Install the required packages using:

```bash
pip install -r requirements.txt
```

---

## Project Structure

```
📁 Project Directory
├── random_forest_model.py
├── label_encoder.py           
├── flask_app.py               # Main Flask app file
├── random_forest_model.pkl     # Pre-trained Random Forest model
├── label_encoder.pkl           # Pre-trained LabelEncoder
├── educational_platform_dataset.csv   # Original dataset
├── educational_platform_dataset_balanced.csv  # Balanced dataset
├── requirements.txt            # List of dependencies
└── README.md                   # Project documentation
```

---

## How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repository-name.git
   cd your-repository-name
   ```

2. Ensure you have the pre-trained model and encoder files (`random_forest_model.pkl` and `label_encoder.pkl`) in the project directory.

3. Run the Flask application:
   ```bash
   python flask_app.py
   ```

4. The application will be available at:
   ```
   http://127.0.0.1:5000/
   ```

---

## API Endpoints

### **1. Health Check**
- **URL**: `/`
- **Method**: `GET`
- **Response**: 
  ```json
  "The ML model API is running successfully!"
  ```

### **2. Predict Field**
- **URL**: `/predict`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "answers": [3, 4, 5, 2, 1, 4, 2, 4, 3, 5, 4, 3, 5, 4, 2, 3, 4, 5, 3, 4]
  }
  ```
- **Response**:
  ```json
  {
    "recommended_field": "Back-End Development"
  }
  ```

---


## License

This project is licensed under the MIT License. Feel free to modify and distribute as per the license terms.

---

## Contact

For queries or contributions:
- **Email**: medo.medo132003@gmail.com
- **GitHub**: [Mohamed Elmahdy](https://github.com/Mohamedelmahdy01)
```
