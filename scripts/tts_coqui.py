import json
from TTS.api import TTS
import soundfile as sf
import os

# Load transcript
with open("transcript.json", "r") as f:
    transcript = json.load(f)

# Init TTS (pick voices you like from Coqui)
reporter_tts = TTS("tts_models/en/ljspeech/tacotron2-DDC")  # neutral/mid
coach_tts = TTS("tts_models/en/ljspeech/tacotron2-DDC")     # you can swap for deeper tone

os.makedirs("audio", exist_ok=True)

# Generate disclosure line
disclosure_text = "This interview was synthetically generated for academic research on September 2, 2025, by Kunal Ahirrao."
disclosure_file = "audio/disclosure.wav"
disclosure_audio = reporter_tts.tts(disclosure_text)
sf.write(disclosure_file, disclosure_audio, 22050)

# Combine reporter & coach lines
reporter_lines = [line["text"] for line in transcript["lines"] if line["speaker"] == "R"]
coach_lines = [line["text"] for line in transcript["lines"] if line["speaker"] == "C"]

reporter_text = " ".join(reporter_lines)
coach_text = " ".join(coach_lines)

sf.write("audio/reporter.wav", reporter_tts.tts(reporter_text), 22050)
sf.write("audio/coach.wav", coach_tts.tts(coach_text), 22050)

print("Generated disclosure.wav, reporter.wav, coach.wav in audio/")
