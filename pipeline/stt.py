import whisper # type: ignore

model = whisper.load_model("base")
result = model.transcribe("audio.mp3")
print(result["text"])
import whisper

def transcribe_audio(audio_path: str, model_name="small"):
    model = whisper.load_model(model_name)
    result = model.transcribe(audio_path)
    return result.get("text","")
