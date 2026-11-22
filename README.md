# Video Remake Pipeline

This is a cloud-based pipeline that takes a video URL, analyzes it with rea-video, and creates a new original video in a similar style using OpenMontage.

## How to use

1. Go to the Actions tab
2. Select "Video Remake Pipeline" 
3. Click "Run workflow"
4. Paste your video URL in the `video_url` field
5. Click "Run workflow"

## What it does

1. Downloads the video
2. Decomposes it frame-by-frame with rea-video
3. Creates a brief of what to keep and what to change
4. Generates 5 hook options for the first 3 seconds
5. Produces a new video using free stock footage, animations, and royalty-free audio

## Output

When done, you'll find in the Artifacts:
- `final.mp4` - Your new video (1080x1920, 9:16 vertical)
- `title.txt`, `description.txt`, `tags.txt` - Publishing metadata
- `thumbnail.jpg` - Thumbnail image

## Secrets

Set these in GitHub Settings → Secrets → Actions:
- `GROQ_API_KEY` - Your Groq API key for the Free LLM API gateway
- `YOUTUBE_COOKIES` - (Optional) YouTube cookies for blocked videos

## Safety

- Artifacts are kept for only 1 day
- Source video is never uploaded
- No personal information is stored in this repo
- Workflow only runs when manually triggered