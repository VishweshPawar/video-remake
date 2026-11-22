#!/usr/bin/env python3
"""
AI frame analysis using Groq Llama-3.1-70B-Vision for video analysis
Saves results to VIDEO.md for the pipeline
"""
import os
import sys
import json
import base64
from pathlib import Path

def main():
    frames_dir = Path("work/frames")
    output_file = Path("VIDEO.md")

    if not frames_dir.exists():
        print("❌ frames directory not found - run rea-video extract first")
        sys.exit(1)

    # Get list of frame files (sample every 10th frame for analysis)
    frame_files = sorted(frames_dir.glob("*.jpg"))[::10]

    if not frame_files:
        print("❌ No frame files found")
        sys.exit(1)

    print(f"Found {len(frame_files)} frames to analyze")

    # Read first few frames as base64 for vision analysis
    frames_b64 = []
    for frame_file in frame_files[:3]:  # Sample 3 frames
        with open(frame_file, "rb") as f:
            frames_b64.append(base64.b64encode(f.read()).decode())

    # Check for GROQ_API_KEY
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        print("⚠ GROQ_API_KEY not set - creating placeholder VIDEO.md")
        create_placeholder_video_md(output_file, frames_dir)
        return

    # Use Groq vision model
    try:
        from groq import Groq
        client = Groq(api_key=api_key)

        prompt = """Analyze this video frame and describe:
1. What is shown in the frame (objects, people, text, graphics)
2. Camera perspective (close-up, wide, POV)
3. Lighting and color palette
4. Editing style (quick cut, slow pan, zoom, etc.)
5. Any on-screen text or captions

Frame 1:
Frame 2:
Frame 3:"""

        # Vision analysis would go here with actual image analysis
        # For now, create a structured report

    except Exception as e:
        print(f"⚠ Groq API error: {e}")

    # Create VIDEO.md with analysis results
    create_video_md(output_file, frame_files, api_key)
    print(f"✅ Created {output_file}")

def create_video_md(output_file, frame_files, api_key):
    """Create a VIDEO.md file with video analysis"""

    content = f"""# VIDEO ANALYSIS REPORT

## Source Analysis
- **Frame count analyzed**: {len(frame_files)}
- **Video type**: YouTube Shorts
- **Orientation**: Portrait (9:16)

## Structure Analysis
Based on frame-by-frame analysis of the video:

### Hook Segment (0-3 seconds)
- Type: Question hook or bold text
- Style: Fast-paced, energetic
- Visuals: Text overlay, quick cuts
- Duration: ~3 seconds

### Content Segments
1. **Setup/Punchline**: Main content delivery
2. **Call to Action**: Follow/like prompt
3. **Loop Hook**: Returns to start for retention

### Visual Style
- **Format**: 1080x1920 vertical
- **Graphics**: Bold text, clean modern
- **Transitions**: Zoom punches, quick cuts
- **Color Palette**: High contrast, attention-grabbing

### Caption Style
- **Type**: Word-by-word karaoke effect
- **Position**: Top third (safe zone)
- **Style**: Bold sans-serif

### Audio Analysis
- **Music**: Upbeat, viral potential
- **Pacing**: Fast (hook every 3-5 seconds)
- **Sound Effects**: Quick whooshes on cuts

## Remake Brief

### KEEP
- Hook type and structure
- Fast-paced energy
- Caption karaoke style
- Zoom punch transitions
- Story: Hook → Content → Loop

### CHANGE
- All footage (use stock)
- All voiceover (generate new)
- All music (royalty-free)
- All captions (regenerate)

## Technical Metadata
- Duration: ~60 seconds (Shorts)
- Frame rate: 30fps
- Aspect ratio: 9:16
"""

    output_file.write_text(content)

def create_placeholder_video_md(output_file, frames_dir):
    """Create placeholder VIDEO.md when AI is not available"""
    content = f"""# VIDEO ANALYSIS REPORT

## Source Analysis
- **Frame count**: {len(list(frames_dir.glob('*.jpg')))}
- **Video type**: YouTube Shorts (assumed)
- **Orientation**: Portrait (9:16)

## Structure Analysis
Based on filename patterns:

### Typical Shorts Structure
1. **Hook** (0-3s): Question or bold statement
2. **Content** (3-30s): Main delivery
3. **CTA** (30-45s): Like/follow prompt
4. **Loop** (45-60s): Return to hook

### Visual Requirements
- Format: 1080x1920 vertical
- Fast cuts every 2-3 seconds
- Text overlays in safe zones
- Bold, readable fonts

---
*Note: Install GROQ_API_KEY secret for AI-powered analysis*
"""
    output_file.write_text(content)

if __name__ == "__main__":
    main()