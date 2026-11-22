"""Text Plagiarism Detector using Cosine Similarity & N-Gram Shingles"""
import math, re
from collections import Counter

def tokenize(text: str):
    return re.findall(r"[a-z0-9]+", text.lower())

def ngrams(tokens, n=3):
    return [" ".join(tokens[i:i+n]) for i in range(max(0, len(tokens) - n + 1))]

def cosine_similarity(text_a: str, text_b: str) -> float:
    ca, cb = Counter(tokenize(text_a)), Counter(tokenize(text_b))
    dot = sum(ca[w] * cb[w] for w in ca)
    na = math.sqrt(sum(v*v for v in ca.values()))
    nb = math.sqrt(sum(v*v for v in cb.values()))
    return round((dot / (na * nb)) * 100, 2) if na and nb else 0.0

def overlap_phrases(text_a: str, text_b: str, n=3):
    return sorted(set(ngrams(tokenize(text_a), n)) & set(ngrams(tokenize(text_b), n)))

if __name__ == "__main__":
    doc1 = "Dynamic programming solves complex problems by breaking them into overlapping subproblems."
    doc2 = "Breaking complex problems into overlapping subproblems is how dynamic programming solves tasks."
    print(f"Similarity Score: {cosine_similarity(doc1, doc2)}%")
    print("Shared 3-gram phrases:", overlap_phrases(doc1, doc2))
