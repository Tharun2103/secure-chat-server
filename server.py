from flask import Flask, request, jsonify

app = Flask(__name__)
messages = []

@app.route("/send", methods=["POST"])
def send():
    data = request.json
    messages.append(data["msg"])
    return {"status": "sent"}

@app.route("/receive", methods=["GET"])
def receive():
    return jsonify(messages)

# 👇 IMPORTANT CHANGE
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)