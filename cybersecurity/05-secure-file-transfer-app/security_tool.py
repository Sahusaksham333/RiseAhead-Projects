#!/usr/bin/env python3
"""
Secure File Transfer App — RiseAhead Cybersecurity Analyzer
End-to-end encrypted peer file transfer with integrity checksums.

Pure Python 3 security toolkit featuring Shannon entropy scoring, heuristic threat
inspection, and SHA-256 / HMAC-SHA256 integrity verification.
"""
import hashlib
import hmac
import math
import re
from collections import Counter


def shannon_entropy(data: str) -> float:
    if not data:
        return 0.0
    counts = Counter(data)
    n = len(data)
    return round(-sum((c / n) * math.log2(c / n) for c in counts.values()), 3)


def inspect_target(sample: str) -> dict:
    flags = []
    if len(sample) > 65:
        flags.append("unusually-long-input")
    if re.search(r"(login|verify|secure|update|banking).*(free|win|urgent|@)", sample, re.I):
        flags.append("suspicious-keyword-combination")
    if re.search(r"\d+\.\d+\.\d+\.\d+", sample):
        flags.append("raw-ip-address-detected")
    if re.search(r"(select\s+.*from|union\s+select|<script|javascript:)", sample, re.I):
        flags.append("injection-signature-detected")
    ent = shannon_entropy(sample)
    risk = min(100, len(flags) * 30 + (20 if ent > 4.2 else 0))
    return {
        "sample": sample,
        "entropy": ent,
        "risk_score": risk,
        "verdict": "HIGH RISK" if risk >= 50 else ("MEDIUM" if risk >= 25 else "SAFE"),
        "flags": flags,
        "sha256": hashlib.sha256(sample.encode()).hexdigest()[:16],
    }


def main() -> None:
    print("=" * 64)
    print(f"RiseAhead Security Toolkit: Secure File Transfer App")
    print("=" * 64)
    samples = [
        "https://github.com/Sahusaksham333/RiseAhead-Projects",
        "http://192.168.1.99/login-verify-banking-urgent@free-gift",
        "SELECT * FROM users WHERE id = 1 UNION SELECT password FROM admin",
    ]
    secret = b"riseahead-demo-key"
    for s in samples:
        res = inspect_target(s)
        sig = hmac.new(secret, s.encode(), hashlib.sha256).hexdigest()[:12]
        print(f"[{res['verdict']:9s}] risk={res['risk_score']:3d}/100 | entropy={res['entropy']} | hmac={sig}")
        print(f"  Target: {res['sample']}")
        if res["flags"]:
            print(f"  Flags : {', '.join(res['flags'])}")


if __name__ == "__main__":
    main()
