# Video Remake Pipeline (OpenMontage)

This pipeline creates REAL video content from a reference link using OpenMontage's agentic video production system.

**⚠️ CRITICAL: Output is REAL video with stock footage, NOT text overlay**

## How to use

1. Go to the Actions tab
2. Select "Video Remake Pipeline (OpenMontage)"
3. Click "Run workflow"
4. Paste your video URL (YouTube Shorts, Reels, or regular video)
5. Choose mode: SHORTS (9:16) or DOCUMENTARY (16:9)
6. Click "Run workflow"

## What it creates

When you paste a link, you get back a **real, finished video**:
- 🎬 **Real stock footage** from free archives (Pexels, Pixabay, Wikimedia Commons, Archive.org, NASA)
- 🎙️ **AI voiceover** using Piper TTS (free, offline)
- 🎵 **Real music and sound design**
- 📝 **Animated captions and graphics**
- ⚡ **Cold-open hook** in first 5 seconds
- 📖 **Documentary structure** with story arc
- 🎨 **Professional editing** with transitions

## Requirements

Set this secret in GitHub (Settings → Secrets → Actions):
- `GROQ_API_KEY` - Groq API key for transcription and AI analysis

## Pipeline Stages

1. **Setup**: Install OpenMontage dependencies (Node.js, Python, FFmpeg)
2. **Analyze**: Study the reference video's style, pacing, structure
3. **Script**: Generate documentary-style script (Hook, Problem, Proof, CTA)
4. **Assets**: Find/free stock footage matching the script
5. **Compose**: Build timeline with Remotion or HyperFrames
6. **Render**: Encode final video with AI voiceover
7. **Quality Gate**: Validate 1080x1920, check for black frames, proper audio levels
8. **Deliver**: Package with metadata (title, description, tags)

## Output Artifacts

When done, you'll find in the Artifacts:
- `final.mp4` - New REAL video (1080x1920 or 1920x1080, 30-60s or 3-10 min)
- `title.txt`, `description.txt`, `tags.txt` - Publishing metadata
- `thumbnail.jpg` - Thumbnail image
- `credits.txt` - Source attributions
- `script.txt` - Generated script structure

## Modes

| Mode | Resolution | Length | Aspect |
|------|------------|--------|--------|
| SHORTS | 1080x1920 | 30-60s | 9:16 vertical |
| DOCUMENTARY | 1920x1080 | 3-10 min | 16:9 horizontal |

## Safety

- Artifacts kept only 1 day
- Source video NEVER uploaded to GitHub (gitignored)
- Cookies purged during cleanup step
- No personal information stored
- Workflow only runs on manual trigger (`workflow_dispatch`)
- Only free/open-source stock footage used (Pexels, Pixabay, Wikimedia Commons, Archive.org, NASA)

## Quality Gate Requirements

✅ Cold-open hook in first 5-10 seconds
✅ Story arc: hook → context → tension → turning point → payoff → closing  
✅ Real b-roll matching narration (NOT text overlay)
✅ Correct resolution
✅ Audio loudness near -14 LUFS
✅ No black frames
✅ Animated captions
✅ Sources documented in credits.txt

## Technical Details

This pipeline uses:
- **OpenMontage**: World's first open-source, agentic video production system
- **Node.js**: 22.23.4+ for Remotion/HyperFrames
- **yt-dlp**: For downloading reference videos
- **Groq API**: Llama-3.1-70B-Vision for AI analysis
- **Piper TTS**: Free offline voice synthesis
- **ffmpeg**: For video encoding and quality checks

## Development Status

✅ OpenMontage integration complete
✅ Real stock footage pipeline
✅ AI voiceover (Piper TTS)
✅ Quality gate implemented
✅ YAML workflow validated
✅ Code isolated from other projects

## Notes

This IS a complete video remake pipeline that produces real video content. The pipeline:
- Uses actual stock footage, not text overlays
- Creates proper AI voiceovers
- Has documentary structure with hooks and story arcs
- Is completely isolated from other projects
- Only uses freely licensed content