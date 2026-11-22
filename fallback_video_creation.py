#!/usr/bin/env python3
"""
Fallback video creation using free stock footage APIs.
Creates REAL video content (not text overlay) when OpenMontage is unavailable.
"""

import os
import sys
import json
import subprocess
import tempfile
import urllib.request
import urllib.parse
from pathlib import Path

def download_file(url: str, output_path: str) -> bool:
    """Download a file from URL to output path."""
    try:
        urllib.request.urlretrieve(url, output_path)
        return True
    except Exception as e:
        print(f"❌ Download failed: {e}")
        return False

def get_stock_footage_pexels(query: str, api_key: str = None) -> dict:
    """Search Pexels for stock footage."""
    base_url = "https://api.pexels.com/videos/search"
    headers = {"Authorization": api_key} if api_key else {}

    params = {
        "query": query,
        "per_page": 5,
        "orientation": "portrait"
    }

    # Without API key, use limited queries
    try:
        import requests
        response = requests.get(base_url, headers=headers, params=params, timeout=10)
        if response.status_code == 200:
            return response.json()
    except:
        pass

    return {"videos": []}

def get_stock_footage_pixabay(query: str) -> dict:
    """Search Pixabay for video footage."""
    base_url = "https://pixabay.com/api/videos/"

    params = {
        "key": "demo",  # Limited without API key
        "q": query,
        "per_page": 5,
        "orientation": "vertical"
    }

    try:
        import requests
        response = requests.get(base_url, params=params, timeout=10)
        if response.status_code == 200:
            return response.json()
    except:
        pass

    return {"hits": []}

def create_video_with_ffmpeg(frames_dir: str, audio_file: str, output: str, mode: str = "SHORTS"):
    """Create video using ffmpeg from downloaded footage and audio."""

    # Get list of video clips
    clips = list(Path(frames_dir).glob("*.mp4"))

    if not clips:
        print("❌ No video clips available")
        return False

    # Create concat file for ffmpeg
    concat_file = Path(frames_dir) / "concat.txt"
    with open(concat_file, "w") as f:
        for clip in sorted(clips):
            f.write(f"file '{clip}'\n")

    duration = 45 if mode == "SHORTS" else 300

    # Build ffmpeg command
    cmd = [
        "ffmpeg",
        "-f", "concat",
        "-safe", "0",
        "-i", str(concat_file),
        "-i", audio_file if os.path.exists(audio_file) else "silent.mp3",
        "-c:v", "libx264",
        "-c:a", "aac",
        "-vf", "scale=1080:1920,format=yuv420p",
        "-t", str(duration),
        "-y", output
    ]

    print(f"Running: {' '.join(cmd)}")

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode == 0:
        print(f"✅ Video created at {output}")
        return True
    else:
        print(f"❌ FFmpeg failed: {result.stderr}")
        return False

def generate_voiceover_with_piper(text: str, output_path: str, voice: str = "en_GB-voice-low"):
    """Generate voiceover using Piper TTS (if available) or silent audio."""

    # Check if piper is available
    piper_path = "/usr/local/bin/piper"  # Common install location
    model_path = "~/.local/share/piper/models/en_GB-low.onnx"

    if os.path.exists(piper_path) or os.path.exists("piper"):
        try:
            cmd = [
                "piper",
                "--model", model_path,
                "--text", text,
                "--output-file", output_path
            ]
            subprocess.run(cmd, check=True)
            print(f"✅ Voiceover generated")
            return True
        except:
            pass

    # Create silent audio as fallback
    print("⚠ Piper TTS not available, creating silent audio")
    silent_cmd = [
        "ffmpeg", "-y", "-f", "lavfi", "-i", "anullsrc=channel_layout=stereo:sample_rate=44100",
        "-t", "5", "-q:a", "9", "-ar", "22050", "-ac", "1", output_path
    ]
    subprocess.run(silent_cmd, capture_output=True)
    return True

def main():
    """Main entry point for fallback video creation."""

    mode = os.environ.get("MODE", "SHORTS")
    script_file = "../script.txt"
    output_path = "../final.mp4"
    work_dir = "../work/fallback"

    print("=== Fallback Video Creation ===")
    print(f"Mode: {mode}")
    print(f"Script file: {script_file}")

    # Create work directory
    os.makedirs(work_dir, exist_ok=True)

    # Parse script to get topics
    topics = []
    if os.path.exists(script_file):
        with open(script_file, 'r') as f:
            content = f.read()
            # Extract simple topics from script
            if "HOOK:" in content:
                topics.append(content.split("HOOK:")[1].split("\n")[0].strip())
            if "TITLE:" in content:
                topics.append(content.split("TITLE:")[1].split("\n")[0].strip())

    if not topics:
        topics = ["technology", "science", "innovation"]  # Default topics

    print(f"Topics to search: {topics}")

    # Download stock footage for each topic
    clips_downloaded = 0
    for i, topic in enumerate(topics[:5]):
        output_clip = os.path.join(work_dir, f"clip_{i}.mp4")

        print(f"Searching for footage: {topic}")

        # Try Pexels first (needs free API key)
        pexels_result = get_stock_footage_pexels(topic)
        if pexels_result.get("videos"):
            video = pexels_result["videos"][0]
            if "video_files" in video:
                url = video["video_files"][0].get("link")
                if url:
                    print(f"Downloading from Pexels: {url}")
                    if download_file(url, output_clip):
                        clips_downloaded += 1
                        continue

        # Try Pixabay
        pixabay_result = get_stock_footage_pixabay(topic)
        if pixabay_result.get("hits"):
            video = pixabay_result["hits"][0]
            if "video" in video:
                url = video["video"]
                print(f"Downloading from Pixabay: {url}")
                if download_file(url, output_clip):
                    clips_downloaded += 1
                    continue

    print(f"Downloaded {clips_downloaded} video clips")

    # Generate voiceover if script has content
    audio_path = os.path.join(work_dir, "voiceover.mp3")
    if os.path.exists(script_file):
        with open(script_file, 'r') as f:
            text = f.read()[:500]  # First 500 chars
        generate_voiceover_with_piper(text, audio_path)
    else:
        # Create silent placeholder
        subprocess.run([
            "ffmpeg", "-y", "-f", "lavfi", "-i", "anullsrc=channel_layout=stereo:sample_rate=44100",
            "-t", "5", audio_path
        ], capture_output=True)

    # Create final video
    if clips_downloaded > 0:
        success = create_video_with_ffmpeg(work_dir, audio_path, output_path, mode)
        if success:
            return 0

    print("❌ Could not create video with available resources")
    return 1

if __name__ == "__main__":
    sys.exit(main())