from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "AIChatBot API is running! 🚀"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    # Пример простого ответа — можешь поменять логику под свой AI
    if not user_message.strip():
        bot_reply = "Please say something 😅"
    else:
        bot_reply = f"You said: {user_message}"

    return jsonify({"reply": bot_reply})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
