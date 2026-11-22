#!/usr/bin/env python3
"""
Network & IoT Security Auditing — RiseAhead IoT Sensor Telemetry & Automation Simulator
Test default credential hygiene on lab IoT devices to harden deployments.

Pure Python 3 edge-node telemetry simulator with threshold alerting and JSON event payloads.
"""
import json
import random
import time


class EdgeSensorNode:
    def __init__(self, node_id: str, warn_threshold: float = 75.0) -> None:
        self.node_id = node_id
        self.warn_threshold = warn_threshold

    def read_telemetry(self) -> dict:
        value = round(random.uniform(22.0, 92.0), 2)
        status = "ALERT" if value >= self.warn_threshold else "OK"
        actuator = "ACTIVATE_CONTROL" if status == "ALERT" else "STANDBY"
        return {
            "node_id": self.node_id,
            "timestamp": int(time.time()),
            "reading": value,
            "status": status,
            "actuator": actuator,
        }


def main() -> None:
    print("=" * 64)
    print(f"RiseAhead IoT Edge Node: Network & IoT Security Auditing")
    print("=" * 64)
    node = EdgeSensorNode(node_id="ESP32-NODE-01", warn_threshold=70.0)
    for tick in range(1, 6):
        payload = node.read_telemetry()
        print(f"[Tick {tick}] {json.dumps(payload)}")


if __name__ == "__main__":
    main()
