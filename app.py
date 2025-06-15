import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from google import genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

app = Flask(__name__)

def chat_with_gemini(prompt):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    return response.text

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    reply = chat_with_gemini(user_message)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
