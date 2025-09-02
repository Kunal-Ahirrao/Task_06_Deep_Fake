# Task_06_Deep_Fake

An ethical, fully-documented workflow to turn a data narrative into a short **synthetic interview** (audio or video) using free/student-friendly tools.

> ⚠️ **Transparency-first**: Every output from this repo is **clearly disclosed** as AI-generated. Do not impersonate real people without explicit consent. Use fictional characters or yourself.

## What this repo gives you
- A **scripted Q&A** you can adapt to your dataset.
- Prompts for LLMs to generate an interview script from a narrative.
- Two implementation paths (choose one or both):
  1) **Audio-only** interview (fast + low friction).
  2) **Talking-head video** using open-source tools.
- A step-by-step **workflow**, plus checklists and an **ethics statement**.
- Commands to **watermark**/label outputs and embed metadata.

## Repo structure
```
Task_06_Deep_Fake/
├─ README.md
├─ data/
│  └─ narrative.md             # Your source narrative (edit this)
├─ prompts/
│  ├─ system_prompt.txt
│  ├─ interviewer_prompt.txt
│  └─ interviewee_prompt.txt
├─ scripts/
│  ├─ 00_requirements.md       # Software you need
│  ├─ 01_workflow_audio_only.md
│  ├─ 02_workflow_video_talking_head.md
│  ├─ 03_watermark_and_metadata.md
│  ├─ 04_email_template_to_instructor.md
│  └─ 05_process_log_template.md
├─ ethics/
│  ├─ ethics_statement.md
│  └─ consent_template.md
├─ audio/                      # Place generated .wav/.mp3 here
├─ video/                      # Place generated .mp4 here
└─ assets/                     # Optional: still image for talking head, logos, etc.
```

## Quick start
1. **Edit** `data/narrative.md` with your own narrative (or keep the template and replace TODOs).
2. Generate a script: use the prompts in `prompts/` (or the included example script below).  
3. Pick a path:
   - **Audio-only**: Use Piper TTS or OpenVoice to create interviewer & guest voices, then mix in Audacity or ffmpeg.
   - **Talking-head video**: Use SadTalker or Wav2Lip to animate a still image with your generated audio.
4. **Watermark/label**: Add a spoken disclosure at the start (2–3 seconds), plus file metadata (see `scripts/03_watermark_and_metadata.md`).
5. **Document your process** in `scripts/05_process_log_template.md` (this is what matters most!).
6. Push to a public GitHub repo named **Task_06_Deep_Fake** and email the link.

## Free/Open tools suggested
- **TTS (offline/local)**: Piper (`piper-tts`) — simple, fast, lots of voices.
- **TTS (voice style/cloning)**: OpenVoice — instant style cloning & multilingual controls.
- **Talking head**: SadTalker — animate a still image from audio.
- **Lip-sync to existing video**: Wav2Lip.
- **Editing**: Audacity (audio), CapCut or DaVinci Resolve (video), or plain `ffmpeg`.
- **Metadata**: `ffmpeg`.

## Ethical use
- Use **fictional names** (e.g., *Coach Morgan Ellis*, *Reporter Jay Singh*).  
- **Do not** clone a real person’s voice or face without explicit, written consent stored in `ethics/`.
- Always include: (a) audible disclosure at start, (b) on-screen label (if video), (c) metadata tags.

## Submission notes
- GitHub repo: **Task_06_Deep_Fake**
- Email link to: **jrstrome@syr.edu**
- Qualtrics check-in: report progress by **2025-09-01** (update date if needed).

---

### Example interview script (fictional characters)
See `data/narrative.md` for context and placeholders you can replace with your actual numbers.

**Reporter (Jay):** Welcome back! Today I’m with Coach **Morgan Ellis** to talk about the upcoming season. Quick reminder: this interview is AI‑generated for research.

**Coach (Ellis):** Thanks, Jay. Happy to chat about what we learned from last season.

**Jay:** If you had to summarize last year in one sentence, what would it be?

**Ellis:** We were **strong in transition** and **efficient on free‑position shots**, but we need to **cut turnovers** and **win more draw controls** to control tempo.

**Jay:** What’s the one metric you want to move first?

**Ellis:** **Draw control percentage**. A small bump there compounds into more possessions, which feeds our pace and shot quality.

**Jay:** You’ve emphasized “shot quality” — what changes?

**Ellis:** We’re creating more **inside looks** and using **early seals** to free cutters. That plus **quicker skip passes** should raise our **expected goals per shot**.

**Jay:** Any defensive adjustments?

**Ellis:** Two: **communication in switch calls** and **closing under 2 seconds** on perimeter dodges. We drilled a “2‑second rule” all camp.

**Jay:** Which players’ roles evolve?

**Ellis:** A sophomore middie steps into **primary draw** duties, and our senior attacker adds **initiations from X** to diversify the set.

**Jay:** What does success look like in the first three games?

**Ellis:** **Fewer unforced turnovers**, **+3 ground balls per game**, and **>50% draw controls**. If we hit those, the wins follow.

**Jay:** Final word to the fans?

**Ellis:** We’re faster, smarter, and **ready to finish close games**. See you out there!

> Add a 2–3s audible disclosure: “This interview was synthetically generated for academic research on 2025-09-01.”

---

