from flask import Flask, request, jsonify
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Initialize the Flask app
app = Flask(__name__)

# Load and preprocess the data
data = pd.read_csv("educational_platform_dataset_balanced.csv")

field_counts = data["Recommended Field"].value_counts()

# Balance the dataset
balanced_data = pd.DataFrame()
for field in field_counts.index:
    field_data = data[data["Recommended Field"] == field]
    balanced_data = pd.concat([
        balanced_data,
        field_data.sample(n=field_counts.max(), replace=True, random_state=42)
    ])

balanced_data = balanced_data.sample(frac=1, random_state=42).reset_index(drop=True)

X = balanced_data.drop("Recommended Field", axis=1)
y = balanced_data["Recommended Field"]

# Encode the labels
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Train the Random Forest model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Function to predict the field
def predict_field(user_answers):
    prediction = model.predict([user_answers])
    field = label_encoder.inverse_transform(prediction)
    return field[0]

# Define the API endpoint
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Parse the input JSON
        user_data = request.json
        user_answers = user_data.get("answers")
        
        if not user_answers or len(user_answers) != X_train.shape[1]:
            return jsonify({"error": "Invalid input data"}), 400

        # Predict the field
        recommended_field = predict_field(user_answers)
        return jsonify({"Recommended Field": recommended_field})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)
