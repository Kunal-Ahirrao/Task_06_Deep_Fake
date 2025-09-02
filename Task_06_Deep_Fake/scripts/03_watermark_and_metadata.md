# Watermarking & metadata

## Audible disclosure
Record or TTS a 2–3s clip and **prepend** it to your interview:
> "This interview is AI-generated for academic research on YYYY-MM-DD."

With ffmpeg (replace files):
```bash
# Join two audio files: disclosure + interview (gapless)
ffmpeg -i audio/disclosure.wav -i audio/interview_mix.mp3 -filter_complex "[0:a][1:a]concat=n=2:v=0:a=1[outa]" -map "[outa]" audio/interview_with_disclosure.mp3
```

## Metadata tags (audio or video)
```bash
ffmpeg -i video/interview.mp4 -c copy -movflags use_metadata_tags   -metadata title="Deep Fake Interview (Research)"   -metadata artist="Your Name (AI-generated)"   -metadata comment="Synthetic media for academic research; non-impersonating; {today}"   video/interview_tagged.mp4
```
Replace paths for audio if needed.
