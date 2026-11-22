#!/usr/bin/env python3
"""
Generate a 4-beat structure script (Hook, Problem, Proof, Loop)
"""
import os
import sys
import json
from pathlib import Path

def main():
    best_hook = ""
    hooks_file = Path("hooks.json")

    if hooks_file.exists():
        with open(hooks_file) as f:
            hooks = json.load(f)
            if hooks:
                best_hook = hooks[0]["hook"]

    if not best_hook:
        best_hook = "What if I told you this simple trick changed everything?"

    api_key = os.environ.get("GROQ_API_KEY")

    if api_key:
        try:
            from groq import Groq
            script_content = generate_ai_script(best_hook, api_key)
        except Exception as e:
            print(f"⚠ AI script generation failed: {e}")
            script_content = generate_default_script(best_hook)
    else:
        print("⚠ GROQ_API_KEY not set - generating default script")
        script_content = generate_default_script(best_hook)

    # Save script
    Path("script.txt").write_text(script_content)
    print(f"✅ Generated script with 4-beat structure")

def generate_ai_script(hook, api_key):
    """Generate script using Groq AI"""
    from groq import Groq
    client = Groq(api_key=api_key)

    prompt = f"""
Generate a complete video script for a 60-second YouTube Shorts video.

Hook: "{hook}"

Use this 4-beat structure:
1. HOOK (0-3s): The title hook
2. PROBLEM (3-15s): What problem this solves
3. PROOF (15-45s): Demonstrate/show the solution
4. LOOP/CTA (45-60s): Call to action that loops back to hook

For each beat, provide:
- Exact text to display
- Visual direction (what to show)
- Timing markers
- Caption style notes

Format as:
[0:00-0:03] HOOK: "text here" (Visual: description)
[0:03-0:15] PROBLEM: "text here" (Visual: description)
[0:15-0:45] PROOF: "text here" (Visual: description)
[0:45-0:60] CTA: "text here" (Visual: description)

Include specific visual directions for:
- Text animations (zoom, fade, typewriter)
- Transitions (cut, swipe, jump)
- Graphics (circles, arrows, highlights)
- Sound effects (whoosh, pop, ding)

Generate a compelling script that will go viral.
"""

    response = client.chat.completions.create(
        model="meta-llama-3.1-70b-vision-preview",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500
    )

    return response.choices[0].message.content.strip()

def generate_default_script(hook):
    """Default script when AI not available"""
    return f"""[0:00-0:03] HOOK: "{hook}" (Visual: Bold text zooms in, whoosh sound)
[0:03-0:08] PROBLEM: "Most people miss this one thing that changes everything" (Visual: Person looking confused, text appears)
[0:08-0:15] SETUP: "Here's what you need to know - it's simpler than you think" (Visual: Simple graphic, countdown animation)
[0:15-0:25] PROOF: "Try this and see the difference for yourself" (Visual: Before/after split screen, checkmark appears)
[0:25-0:30] PUNCH: "That's it - just like that" (Visual: Explosion graphic, ding sound)
[0:30-0:35] CTA: "Hit follow for more tips like this!" (Visual: Follow button graphic)
[0:35-0:40] LOOP HOOK: "What if I told you this simple trick changed everything?" (Visual: Text loops back to start)
[0:40-0:60] EXTENSION: "Save this for later and share with a friend who needs this" (Visual: Save/share icons, looping arrow)

Caption timing: Each word appears with 0.1s delay for karaoke effect
Transition: 0.3s wipe between beats
Sound effects: Whoosh on zooms, ding on checkmarks, pop on text
"""

if __name__ == "__main__":
    main()