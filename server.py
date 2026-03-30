from flask import Flask, request, jsonify
from flask_cors import CORS   # 👈 ADD THIS

app = Flask(__name__)
CORS(app)   # 👈 ADD THIS

messages = []

@app.route("/send", methods=["POST"])
def send():
    data = request.json
    messages.append(data)
    return {"status": "sent"}

@app.route("/receive", methods=["GET"])
def receive():
    return jsonify(messages)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
