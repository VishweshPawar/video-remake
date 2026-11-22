#!/usr/bin/env python3
"""
Generate 5 hook options using Groq and score them with hookscore logic
"""
import os
import sys
import json
from pathlib import Path

def main():
    video_md_path = Path("VIDEO.md")
    hooks_file = Path("hooks.json")

    if not video_md_path.exists():
        print("❌ VIDEO.md not found")
        sys.exit(1)

    # Read video analysis
    video_content = video_md_path.read_text()

    # Get API key
    api_key = os.environ.get("GROQ_API_KEY")

    if not api_key:
        print("⚠ GROQ_API_KEY not set - generating default hooks")
        hooks = generate_default_hooks()
    else:
        hooks = generate_ai_hooks(video_content, api_key)

    # Score hooks
    scored_hooks = []
    for hook in hooks:
        score = calculate_hookscore(hook)
        scored_hooks.append({
            "hook": hook,
            "score": score
        })

    # Sort by score descending
    scored_hooks.sort(key=lambda x: x["score"], reverse=True)

    # Save results
    hooks_file.write_text(json.dumps(scored_hooks, indent=2))

    print(f"\n=== HOOK SCORES ===")
    for h in scored_hooks:
        print(f"Score {h['score']}/100: {h['hook'][:60]}...")

    best_hook = scored_hooks[0]["hook"]
    print(f"\n✅ Best hook (score {scored_hooks[0]['score']}/100): {best_hook}")

    # Save best hook
    Path("best_hook.txt").write_text(best_hook)

def generate_default_hooks():
    """Fallback hooks when AI not available"""
    return [
        "What if I told you this simple trick changed everything?",
        "You won't believe what happens when you try this",
        "The answer is shocking - here's what they don't tell you",
        "Can you guess what this is? The reveal will surprise you",
        "This changed my life - here's the one thing everyone should know"
    ]

def generate_ai_hooks(video_analysis, api_key):
    """Generate hooks using Groq AI"""
    try:
        from groq import Groq
        client = Groq(api_key=api_key)

        prompt = f"""
Based on this video analysis, generate 5 unique, attention-grabbing hook options for the first 3 seconds of a YouTube Shorts video.

Video analysis: {video_analysis[:500]}

Each hook should be:
- Maximum 8 words
- Creates instant curiosity
- Works for any content type
- Has viral potential

Return JSON array only, no other text:
["Hook 1", "Hook 2", "Hook 3", "Hook 4", "Hook 5"]
"""

        response = client.chat.completions.create(
            model="meta-llama-3.1-70b-vision-preview",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200
        )

        content = response.choices[0].message.content.strip()
        # Parse JSON from response
        import ast
        hooks = ast.literal_eval(content)
        return hooks

    except Exception as e:
        print(f"⚠ AI hook generation failed: {e}")
        return generate_default_hooks()

def calculate_hookscore(hook):
    """
    Calculate hook score based on multiple factors
    Returns score 0-100
    """
    score = 0

    # Length factor (6-8 words ideal)
    words = len(hook.split())
    if 6 <= words <= 8:
        score += 20
    elif 5 <= words <= 9:
        score += 15
    else:
        score += 10

    # Question mark (curiosity trigger)
    if "?" in hook:
        score += 15

    # Power words (high-impact words)
    power_words = ["what if", "won't believe", "shocking", "secret", "trick",
                   "changed", "everything", "surprise", "reveal", "proven"]
    hook_lower = hook.lower()
    for word in power_words:
        if word in hook_lower:
            score += 8

    # Urgency/CTA words
    urgency_words = ["now", "today", "instant", "quick", "fast", "immediate"]
    for word in urgency_words:
        if word in hook_lower:
            score += 5

    # Number potential (numbers often perform well)
    import re
    if re.search(r'\d+', hook):
        score += 10

    # All caps or exclamation (attention but can be spammy)
    if "!" in hook:
        score += 5

    # Too long penalty
    if len(hook) > 80:
        score -= 10

    # Must be under 100
    return min(100, max(0, score))

if __name__ == "__main__":
    main()