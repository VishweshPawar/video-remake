# Video Remake — Project Instructions

This project remakes videos from a reference link using OpenMontage to create REAL video content.

## Isolation Rules

This project is COMPLETELY SEPARATE from all clipping projects.

- **NEVER** import any logic from cloud-clipper, yt-dlp projects, or any other project
- **NEVER** read or use viral scoring, moment ranking, or clip selection logic from other projects
- **NEVER** access secrets from other projects
- This is a video REMAKING tool, not a clipping tool
- All files stay inside C:\claudepro\video-remake
- Git remote is: https://github.com/VishweshPawar/video-remake.git

## How It Works

1. You paste a YouTube Shorts/TikTok/Reel URL
2. I run the GitHub Actions workflow
3. OpenMontage creates a REAL video with:
   - Real stock footage from Pexels, Pixabay, Wikimedia Commons, Archive.org, NASA
   - AI voiceovers using Piper TTS (free, offline)
   - Real music, sound effects, animated captions and graphics
   - Cold-open hook in first 5 seconds
   - Documentary story arc with open loops
4. You download the finished `final.mp4` artifact

## Modes

| Mode | Resolution | Length | Aspect |
|------|------------|--------|--------|
| SHORTS | 1080x1920 | 30-60s | 9:16 vertical |
| DOCUMENTARY | 1920x1080 | 3-10 min | 16:9 horizontal |

## Pipeline Steps

1. **Setup**: Install OpenMontage + deps (Node 22.x, Python, FFmpeg)
2. **Analyze**: Download video, check if live stream, warn about copyright
3. **Script**: Generate 4-beat structure (Hook/Problem/Proof/CTA) with Groq
4. **Assets**: Find matching free stock footage
5. **Compose**: Build timeline with Remotion/HyperFrames
6. **Render**: Encode with AI voiceover + music
7. **Quality Gate**: Check frames aren't text overlay, validate resolution
8. **Deliver**: Package with metadata, credits, thumbnail

## GitHub Secrets Required

| Secret | Purpose |
|--------|---------|
| `GROQ_API_KEY` | Script generation and video analysis |
| `NODE_VERSION` | Optional: Node.js version (default: 22.23.4) |

## Quality Gate Requirements

✅ Cold-open hook in first 5 seconds
✅ Story arc: hook → context → tension → turning point → payoff → closing
✅ Open loops for engagement (documentary mode)
✅ Fact-checked script with sources.md
✅ Real footage (not text overlay) - verified by frame analysis
✅ 1080x1920 (SHORTS) or 1920x1080 (DOCUMENTARY)
✅ Animated captions (word-by-word karaoke effect)
✅ Audio loudness near -14 LUFS
✅ No black frames
✅ Sources documented in credits.txt

## Related Files

- `.github/workflows/video-remake.yml` - Main GitHub Actions workflow
- `scripts/generate_script.py` - Create 4-beat documentary script
- `scripts/analyze_frames.py` - Frame analysis with Groq vision
- `fallback_video_creation.py` - Stock footage fallback if OpenMontage fails
- `.claude/skills/remake-video/SKILL.md` - Skill for invoking this pipeline

## Usage

When you paste a link, say "go" and I'll:
1. Trigger the GitHub Actions workflow with the URL
2. Wait for completion
3. Download the artifact
4. Verify the video is real (not text overlay)
5. Show you the results