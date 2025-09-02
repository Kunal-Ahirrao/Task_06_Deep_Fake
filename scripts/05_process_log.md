# Process Log — Task 06 (Kunal Ahirrao)

- Dataset: SU Women’s Lacrosse (Task 05 repo)
- Time window: Aug 28–Sep 2, 2025
- Total time spent: ~5–7 hours

## Steps I took
1) Re‑read Task 05 results (`lacrosse_summary_stats.json`) and pulled season snapshot.
2) Wrote a narrative focusing on close games, shot quality, and possession levers.
3) Prompted an LLM with my narrative to draft a 2‑minute, 10‑Q&A script.
4) Edited lines to keep numbers grounded (no new stats invented).
5) Generated audio (separate lines for reporter/coach) and also exported a single mixed MP3.
6) Added disclosure audio at the start and wrote on‑screen label instructions.
7) Documented ethical guardrails and included a consent template.
8) Prepared video options (SadTalker/Wav2Lip) but kept video optional to stay within free tools.

## Tools tried
- LLM: ChatGPT (prompt files in `prompts/`)
- Audio: Piper TTS (local) explored; final audio assembled and included
- Editing: ffmpeg for simple mixing; Audacity tested for timing
- (Optional) Video: readme notes for SadTalker/Wav2Lip; not required for submission

## What worked
- Keeping reporter/coach on **separate WAVs** made timing adjustments easy.
- A short **audible disclosure** reduced any confusion and satisfied ethics requirements.

## What didn’t work (or needed tweaks)
- Some TTS voices sounded robotic at default speed; slowing speech rate helped.
- Auto-lip‑sync looked uncanny on fast phrases; shorter sentences solved it.

## Ethics/consent
- No real person was impersonated. Names used: Reporter **Kunal Ahirrao**, Coach **Regy Thorpe**.
- Clear disclosure at the start of audio; instructions for on‑screen labels in video.
- Consent template added in case real likeness/voice is ever used.

## Reflection — what I learned
- Translating raw stats into a conversational narrative is a powerful way to communicate insights.
- I practiced a full synthetic media workflow end‑to‑end (data → script → audio → optional video) with free tools.
