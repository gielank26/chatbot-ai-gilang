from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
from config import GOOGLE_AI_KEY, text_generation_config, safety_settings

app = Flask(__name__)

genai.configure(api_key=GOOGLE_AI_KEY)
model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    generation_config=text_generation_config,
    safety_settings=safety_settings
)

chat = model.start_chat()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/chat", methods=["POST"])
def chat_api():
    user_message = request.json.get("message")
    response = chat.send_message(user_message)
    return jsonify({"reply": response.text})

if __name__ == "__main__":
    app.run(debug=True)
