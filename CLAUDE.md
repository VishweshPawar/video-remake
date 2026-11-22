# Video Remake — Project Instructions

This project remakes videos (shorts and documentaries) from a reference link.

## Isolation Rules

This project is separate from the clipping projects.

- **NEVER** import clipping logic from cloud-clipper or any other project
- **NEVER** use yt-dlp download scripts, chat reading, or virality scoring from clippers
- **NEVER** touch other repos or their secrets
- This is a video remake tool, not a clipper

## How It Works

1. Takes a YouTube Shorts/TikTok/Reel URL as reference
2. Uses OpenMontage to create a REAL video remake with:
   - Real footage from free stock archives (Pexels, Pixabay, Wikimedia Commons, Archive.org, NASA)
   - AI voiceovers (free Piper voices)
   - Professional editing, transitions, graphics
   - Real music and sound design
3. Outputs a complete vertical (9:16) video with:
   - Cold-open hook in first 5-10 seconds
   - Story arc: hook → context → tension → turning point → payoff → closing
   - Animated captions
   - Sound design and music

## Pipeline

1. **Setup**: Install OpenMontage dependencies (Node.js, Python, FFmpeg)
2. **Analyze**: Study the reference video's style, pacing, structure
3. **Script**: Generate documentary-style script (Hook, Problem, Proof, CTA)
4. **Assets**: Find/free stock footage matching the script
5. **Compose**: Build timeline with Remotion or HyperFrames
6. **Render**: Encode final video with AI voiceover
7. **Quality Gate**: Validate 1080x1920, check for black frames, proper audio levels
8. **Deliver**: Package with metadata (title, description, tags)

## Secrets (GitHub Repo Only)

- `GROQ_API_KEY` - For transcription and AI analysis
- `NODE_VERSION` - Node.js version (default: 22.23.4)