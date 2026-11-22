# Remake-Video Skill

Use this skill when the user pastes a video URL and wants a real video remake.

## When to use

- User pastes a YouTube Shorts, TikTok, or Reel link
- User asks to "remake this video" or "create something from that video"
- User wants viral shorts or documentary-style content

## What this does

Turns a reference video link into a REAL finished video with:
- Stock footage from free archives (Pexels, Pixabay, Wikimedia Commons, Archive.org, NASA)
- AI voiceover using Piper TTS (free, offline)
- Real music and sound design
- Animated captions and graphics
- Cold-open hook in first 5 seconds
- Professional editing with transitions

## How to use

1. Get the video URL from the user
2. Run the GitHub Actions workflow: `.github/workflows/video-remake.yml`
3. The output is a real video file, not text overlay

## Output

When done, you get in the artifacts:
- `final.mp4` - Real video with footage, voiceover, music
- `title.txt`, `description.txt`, `tags.txt` - Publishing metadata
- `thumbnail.jpg` - Thumbnail image
- `credits.txt` - Source attributions
- `script.txt` - Generated script structure

## Important notes

- **NOT a text-overlay video** - This creates real video content
- **Requires GROQ_API_KEY** - Set as GitHub secret
- **Uses only free/open-source assets** - Compliant with licenses
- **Cold-start on new URLs** - Wait for full pipeline completion

## Example invocation

User: "Hey check out this video: https://youtube.com/shorts/abc123"

Me: "I'll remake that video for you. Let me run the pipeline..."
(then trigger the GitHub Actions workflow)

## Quality check

Before saying "done":
- Is final.mp4 1080x1920 (or 1920x1080 for documentary)?
- Does it have actual video footage (not just text overlay)?
- Are captions animated, not static?
- Is the script.txt populated?

## Troubleshooting

- If workflow fails, check GitHub Actions logs
- If GROQ_API_KEY error, user needs to add the secret to their repo
- If video is black, check for download issues in logs
- If no voiceover, Piper TTS may not be installed (silent audio fallback)

## Related skills

- `youtube-clip-pipeline-disabled` - For clipping, not remaking
- `clip` - For downloading and converting clips

## Configuration

Mode options:
- SHORTS: Vertical 9:16 (30-60 seconds)
- DOCUMENTARY: Horizontal 16:9 (3-10 minutes)