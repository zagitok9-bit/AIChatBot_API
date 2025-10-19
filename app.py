from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "")
    if not message:
        return jsonify({"reply": "⚠️ Empty message received."})
    
    # Пример простой обработки:
    reply = f"🤖 AI: I received your message → '{message}'"
    return jsonify({"reply": reply})

if __name__ == "__main__":
    # Railway автоматически подставит PORT из окружения
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
