from flask import Flask, request, jsonify
from gpt4all import GPT4All

app = Flask(__name__)
model = GPT4All("./orca-mini-3b-gguf2-q4_0.gguf", device='cpu')

@app.route("/api/chat", methods = ["POST"])
def chat():
    data = request.json
    message = data.get("message", "")
    response = model.predict(message)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)