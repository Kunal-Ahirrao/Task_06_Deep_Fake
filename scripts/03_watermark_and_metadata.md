# Watermark & metadata

## Embed metadata into MP3/MP4
```bash
ffmpeg -i audio/interview_mix.mp3 -c copy -metadata title="Deep Fake Interview (Research)" \  -metadata artist="Kunal Ahirrao (AI-generated)" \  -metadata comment="Synthetic media for academic research; created on 2025-09-02" audio/interview_mix_tagged.mp3
```
