# Flash backend

from flask import Flask, request, jsonify
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/analyze", methods=["GET", "POST"])
def analyze():
    print("Request.files:", request.files)
    
    screenshot = request.files.get("screenshot")

    if screenshot:
        print("Screenshot received:", screenshot.filename)
    else:
        print("No screenshot received.")

    return jsonify({
        "status": "success",
        "message": "Files received",
        "filename": screenshot.filename if screenshot else None
    })

@app.route("/transcribe", methods=["POST"])
def transcribe():
    audio = request.files.get("audio")
    if audio:
        transcript = openai.Audio.transcribe("whisper-1", audio)
        return jsonify({"status": "success", "transcript": transcript["text"]})
    return jsonify({"status": "fail", "message": "No audio file received."})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5050)

