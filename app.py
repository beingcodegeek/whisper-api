from flask import Flask, request, jsonify
import whisper
import os

app = Flask(__name__)
model = whisper.load_model("base")

@app.route("/transcribe", methods=["POST"])
def transcribe():
    file = request.files['file']
    file.save("temp.mp3")
    result = model.transcribe("temp.mp3")
    os.remove("temp.mp3")
    return jsonify({"text": result["text"]})
