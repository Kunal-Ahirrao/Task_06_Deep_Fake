# Audio‑only workflow

## Files in this repo
- `audio/disclosure.wav` — spoken disclosure (replace if you generate a new one)
- `audio/reporter.wav` — Reporter (Kunal) lines, single file
- `audio/coach.wav` — Coach (Regy) lines, single file
- `audio/interview_mix.mp3` — full stitched interview (already provided)

## If you want to (re)generate audio with Piper TTS
Example (replace model names with installed voices):
```bash
# Disclosure
piper --model en_US-amy-medium --output_file audio/disclosure.wav \
  --text "This interview was synthetically generated for academic research on September 2, 2025, by Kunal Ahirrao."

# Reporter (Kunal) lines
piper --model en_US-amy-medium --output_file audio/reporter.wav \  --text-file scripts/reporter_lines.txt

# Coach (Regy) lines
piper --model en_US-joe-medium --output_file audio/coach.wav \  --text-file scripts/coach_lines.txt
```

## Mix tracks with ffmpeg
```bash
# Example: simple concat with short silences between speakers
ffmpeg -i audio/disclosure.wav -i audio/reporter.wav -i audio/coach.wav   -filter_complex "[1]adelay=2000|2000[a1];[2]adelay=4000|4000[a2];[0][a1][a2]amix=inputs=3:dropout_transition=0[outa]"   -map "[outa]" -c:a mp3 audio/interview_mix.mp3
```
