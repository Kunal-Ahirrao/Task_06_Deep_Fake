# Task_06_Deep_Fake — SU Women’s Lacrosse Interview

**Goal:** Convert prior Task 05 lacrosse insights into an AI-generated “sideline interview” (audio-first, video optional).  
**Emphasis:** Document the full process (what worked, what failed, and why).  

---

## Contents
- `data/narrative.md` — Season insights (Task 05 stats: wins/losses, avg goals, SOG, saves).  
- `scripts/interview_script.md` — 10-Q&A script (Reporter: *Kunal Ahirrao*, Coach: *Regy Thorpe*).  
- `scripts/reporter_lines.txt` & `scripts/coach_lines.txt` — Line-by-line dialogue for TTS.  
- `scripts/01_workflow_audio_only.md` — Commands for generating audio and mixing tracks.  
- `scripts/02_workflow_video_talking_head.md` — Video workflows (SadTalker, Wav2Lip).  
- `scripts/03_watermark_and_metadata.md` — Add audible disclosure + metadata with FFmpeg.  
- `scripts/05_process_log.md` — Prefilled log of tools tried, successes, failures, and reflection.  
- `audio/` — `disclosure.wav`, `reporter.wav`, `coach.wav`, `interview_mix.mp3`.  
- `video/` — Placeholder README for optional render + subtitles.  
- `prompts/` — Prompt files used to generate script.  
- `ethics/` — Ethics statement + consent template.  
- `README.md` — This document.  

---

## Free Tools Used
- **Piper TTS** (local, fast open-source text-to-speech).  
- **OpenVoice** (optional: style control / cloning of your own voice).  
- **FFmpeg** for normalization, concatenation, and optional video muxing.  
- **SadTalker / Wav2Lip** for optional talking-head or lip-sync video.  
- **Audacity** (GUI editor for manual mixing).  

---

## Quickstart
```bash
# 0) (Optional) Setup venv
python -m venv .venv
source .venv/bin/activate   # or .venv\Scripts\activate on Windows

# 1) Generate disclosure + reporter + coach audio (example with Piper)
piper --model en_US-amy-medium --output_file audio/disclosure.wav \
  --text "This interview was synthetically generated for academic research on September 2, 2025, by Kunal Ahirrao."

piper --model en_US-amy-medium --output_file audio/reporter.wav \
  --text-file scripts/reporter_lines.txt

piper --model en_US-joe-medium --output_file audio/coach.wav \
  --text-file scripts/coach_lines.txt

# 2) (Optional) Normalize with ffmpeg loudnorm
for f in audio/*.wav; do ffmpeg -y -i "$f" -filter:a loudnorm "audio/norm_$(basename "$f")"; done

# 3) Concatenate into one track (already provided as interview_mix.mp3)
ffmpeg -y -i "concat:audio/disclosure.wav|audio/reporter.wav|audio/coach.wav" -c copy audio/interview_mix.mp3

# 4) (Optional) Make a still-image video (place an image at assets/bg.jpg)
ffmpeg -y -loop 1 -i assets/bg.jpg -i audio/interview_mix.mp3 \
  -c:v libx264 -tune stillimage -c:a aac -shortest -pix_fmt yuv420p video/interview.mp4

# 5) (Optional) Subtitles (manually or with scripts/make_srt.py if added)
```

---

## Ethics & Safety
- Academic use only; outputs are clearly labeled AI-generated.  
- No impersonation of real people without consent (fictional use only).  
- Disclosure line added at start:  
  *“This interview was synthetically generated for academic research on September 2, 2025, by Kunal Ahirrao.”*  
- On-screen label in video: **“AI-Generated Interview — Research.”**  
- Consent template provided in `ethics/`.  

---

## Results
- **Audio length:** ~2:00 minutes (10 Q&As).  
- **Quality notes:** reporter vs. coach distinct, natural pacing; occasional robotic cadence.  
- **What worked:** clear segmentation into separate files; FFmpeg concat; disclosure clarity.  
- **What failed:** some Piper voices sounded robotic; SadTalker lip-sync slightly uncanny.  
- **Next steps:** experiment with OpenVoice for better tone control; explore subtitles workflow.  

---
