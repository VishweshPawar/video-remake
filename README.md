# Video Remake Pipeline

This is a cloud-based pipeline that takes a YouTube Shorts URL and creates a new original video using AI analysis and ffmpeg.

## How to use

1. Go to the Actions tab
2. Select "Video Remake Pipeline"
3. Click "Run workflow"
4. Paste your video URL (YouTube Shorts) in the `video_url` field
5. Click "Run workflow"

## What it does (Complete 8-Stage Pipeline)

1. **Setup**: Install dependencies (ffmpeg, Python, yt-dlp, groq, etc.)
2. **Download**: Fetch video using yt-dlp with cookie support
3. **Decompose**: Run rea-video for frame extraction
4. **Analyze**: AI frame analysis with Groq Llama-3.1-70B-Vision
5. **Generate Hooks**: Create 5 hooks, score with hookscore.py, pick best
6. **Generate Script**: Create 4-beat structure (Hook/Problem/Proof/CTA)
7. **Create Video**: Render 30s vertical video with ffmpeg + AI content
8. **Quality Gate**: Validate 1080x1920, test frame analysis, generate metadata

## AI Scripts (in `scripts/` folder)

- `analyze_frames.py` - Groq Llama-3.1-70B-Vision frame analysis
- `generate_hooks.py` - AI hook generation with hookscore scoring
- `generate_script.py` - 4-beat structure script generation
- `analyze_frames_for_quality.py` - Quality gate analysis

## Output

When done, you'll find in the Artifacts:
- `final.mp4` - New video (1080x1920, 9:16 vertical, 30s)
- `title.txt`, `description.txt`, `tags.txt` - Publishing metadata
- `thumbnail.jpg` - Thumbnail image
- `hooks.json` - All hook options with scores
- `script.txt` - 4-beat structure script
- `quality_report.md` - Frame-by-frame quality analysis

## Secrets

Set these in GitHub:
1. Go to Settings → Developer settings → Personal access tokens
2. Click "Generate new token"
3. Select `api:text` scope
4. Copy the token
5. In the repo, go to Settings → Secrets → Actions
6. Add `GROQ_API_KEY` with your token

Optional:
- `YOUTUBE_COOKIES` - For blocked videos

## Safety

- Artifacts kept only 1 day
- Source video NEVER uploaded to GitHub (gitignored)
- Cookies purged during cleanup step
- No personal information stored
- Workflow only runs on manual trigger (`workflow_dispatch`)

## Technical Notes

This pipeline uses:
- **rea-video** for frame-by-frame video analysis
- **yt-dlp** for video downloading
- **Groq API** with Llama-3.1-70B-Vision for AI analysis
- **ffmpeg** for video rendering

## Development Status

✅ All 8 pipeline stages complete
✅ AI Python scripts created and tested
✅ YAML workflow validated
✅ Code pushed to public repo
✅ Public repo status: **PUBLIC**
✅ Security checks implemented
✅ Source video cleanup on completion

## Notes

This is NOT a perfect remake pipeline. It creates a text-based video with the hook as overlay. For full OpenMontage integration (stock footage, AI voiceovers, professional editing), you would need:

1. OpenMontage Node.js environment
2. Stock footage licensing
3. AI voice synthesis (ElevenLabs/TTS)

The current pipeline demonstrates the concept and provides a foundation for enhancement.