import gradio as gr
import whisper

model = whisper.load_model("tiny")

def transcribe(audio):
    result = model.transcribe(audio)
    return result["text"]

gr.Interface(
    fn=transcribe,
    inputs=gr.Audio(source="upload", type="filepath"),
    outputs="text",
    title="Whisper Speech Transcription"
).launch()
