"""Lightweight N-Gram Language Detection Engine"""
import re

PROFILES = {
    "English": {"the", "and", "is", "of", "to", "in", "that", "for", "with", "this"},
    "Spanish": {"el", "la", "de", "que", "y", "en", "un", "por", "con", "para"},
    "French":  {"le", "la", "de", "et", "est", "en", "un", "pour", "dans", "que"},
    "German":  {"der", "die", "und", "in", "den", "von", "zu", "das", "mit", "ist"},
    "Hindi (Romanized)": {"hai", "aur", "mein", "ka", "ki", "ke", "ko", "se", "yeh", "hum"},
}

def detect_language(text: str) -> tuple[str, float]:
    words = re.findall(r"[a-z]+", text.lower())
    if not words: return "Unknown", 0.0
    scores = {lang: sum(1 for w in words if w in vocab) for lang, vocab in PROFILES.items()}
    best = max(scores, key=scores.get)
    conf = round((scores[best] / len(words)) * 100, 1)
    return (best, conf) if scores[best] > 0 else ("Unknown", 0.0)

if __name__ == "__main__":
    for s in ["This is a clean Python project for language detection.", "Le chat est dans la maison."]:
        print(s, "->", detect_language(s))
