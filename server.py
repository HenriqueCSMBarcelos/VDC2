from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Allows frontend to access the backend

OLLAMA_URL = "http://localhost:11434/api/generate"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    prompt = data.get("prompt", "")

    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    response = requests.post(OLLAMA_URL, json={"model": "deepseek", "prompt": prompt})

    return jsonify(response.json())

if __name__ == "__main__":
    app.run(debug=True, port=5000)
