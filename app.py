import pickle
from flask import Flask, request, jsonify

MODEL_FILE = "random_forest_model.pkl"  
ENCODER_FILE = "label_encoder.pkl"      
with open(MODEL_FILE, "rb") as model_file:
    model = pickle.load(model_file)

with open(ENCODER_FILE, "rb") as encoder_file:
    label_encoder = pickle.load(encoder_file)

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "The ML model API is running successfully!", 200

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        answers = data.get("answers")

        if not answers or not isinstance(answers, list) or len(answers) != 20:
            return jsonify({"error": "Invalid input. Please provide a list of 20 answers."}), 400

        prediction = model.predict([answers])
        recommended_field = label_encoder.inverse_transform(prediction)[0]

        return jsonify({"recommended_field": recommended_field})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
