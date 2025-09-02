# Audio-only workflow

## 1) Prepare your script
- Start from `README.md` example or generate via `/prompts`.
- Add a **2–3s disclosure** at the start: "This interview was synthetically generated for academic research on YYYY-MM-DD."

## 2) Generate voices
### Option A — Piper (simple, offline)
1. Install:
   ```bash
   pip install piper-tts
   ```
2. Download a voice (see Piper docs for voices). Example command (replace with your voice file path):
   ```bash
   piper --model en_US-amy-medium --output_file audio/reporter.wav --text "Your reporter lines here"
   piper --model en_US-joe-medium --output_file audio/coach.wav    --text "Your coach lines here"
   ```

### Option B — OpenVoice (style control / cloning)
- Follow the OpenVoice README to set up the environment and generate speech from text.
- Use **your own** reference or a **consenting** speaker.
- Export each speaker track separately to `audio/`.

## 3) Assemble the dialogue
Using ffmpeg:
```bash
# Example: concatenate two WAV files with short pause
ffmpeg -i audio/reporter.wav -i audio/coach.wav -filter_complex "acrossfade=d=0.15" -c:a mp3 audio/interview_mix.mp3
```

Or use **Audacity** to drop clips on two tracks, trim silences, and export to MP3.

## 4) Watermark + metadata
See `03_watermark_and_metadata.md` to:
- prepend an audible disclosure clip
- embed metadata in the MP3 (title, artist, comment noting it's synthetic).

## 5) Document your process
Fill out `05_process_log_template.md` and push to GitHub.
