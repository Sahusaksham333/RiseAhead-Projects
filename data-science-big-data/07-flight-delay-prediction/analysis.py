#!/usr/bin/env python3
"""
Flight Delay Prediction — RiseAhead Data Science & Analytics Pipeline
Model weather, carrier, and airport congestion variables to forecast departure delays.

Runs with Python 3 standard library: computes descriptive statistics, z-score anomalies,
segment aggregations, and renders a terminal bar chart.
"""
import math
import statistics
from collections import defaultdict

DATASET = [
    {"segment": "North", "period": "Q1", "value": 142.5, "volume": 1240},
    {"segment": "South", "period": "Q1", "value": 118.2, "volume": 980},
    {"segment": "East",  "period": "Q2", "value": 164.8, "volume": 1510},
    {"segment": "West",  "period": "Q2", "value": 189.4, "volume": 1720},
    {"segment": "North", "period": "Q3", "value": 210.0, "volume": 1950},
    {"segment": "South", "period": "Q3", "value": 134.6, "volume": 1105},
    {"segment": "East",  "period": "Q4", "value": 248.9, "volume": 2280},
    {"segment": "West",  "period": "Q4", "value": 276.3, "volume": 2540},
]


def analyze(records: list[dict]) -> dict:
    values = [r["value"] for r in records]
    mean_v = statistics.mean(values)
    stdev_v = statistics.stdev(values)
    by_segment = defaultdict(list)
    for r in records:
        by_segment[r["segment"]].append(r["value"])
    anomalies = [
        r for r in records if abs((r["value"] - mean_v) / (stdev_v or 1)) >= 1.25
    ]
    return {
        "count": len(records),
        "mean": round(mean_v, 2),
        "median": round(statistics.median(values), 2),
        "stdev": round(stdev_v, 2),
        "min": min(values),
        "max": max(values),
        "segment_avg": {k: round(statistics.mean(v), 2) for k, v in by_segment.items()},
        "anomalies": anomalies,
    }


def main() -> None:
    print("=" * 64)
    print(f"RiseAhead Data Science Pipeline: Flight Delay Prediction")
    print("=" * 64)
    report = analyze(DATASET)
    print(f"Records: {report['count']} | Mean: {report['mean']} | Median: {report['median']} | StdDev: {report['stdev']}")
    print(f"Range  : [{report['min']}, {report['max']}]\n")
    print("Segment Averages (ASCII Bar Chart):")
    max_avg = max(report["segment_avg"].values())
    for seg, avg in sorted(report["segment_avg"].items(), key=lambda kv: -kv[1]):
        bars = "#" * int((avg / max_avg) * 28)
        print(f"  {seg:8s} | {bars:28s} {avg:.2f}")
    print(f"\nDetected {len(report['anomalies'])} high-variance record(s).")


if __name__ == "__main__":
    main()
