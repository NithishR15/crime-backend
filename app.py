from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)

# Allow frontend connection
CORS(app)

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Crime Prediction System Running Online"
    })

@app.route("/predict", methods=["GET"])
def predict():
    return jsonify({
        "result": "Low Crime Area"
    })

# For local testing only
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )
