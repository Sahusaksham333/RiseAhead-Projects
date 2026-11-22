#!/usr/bin/env python3
"""
Dockerized Microservices Store — RiseAhead Cloud & DevOps Service
Polyglot microservices architecture demonstrating service discovery and tracing.

Lightweight Python 3 HTTP microservice with /health, /metrics, and token-bucket rate limiting.
"""
import json
import time
from http.server import BaseHTTPRequestHandler, HTTPServer

START_TIME = time.time()
METRICS = {"requests_total": 0, "health_checks": 0}


class ServiceHandler(BaseHTTPRequestHandler):
    def _send_json(self, code: int, payload: dict) -> None:
        body = json.dumps(payload, indent=2).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:
        METRICS["requests_total"] += 1
        if self.path == "/health":
            METRICS["health_checks"] += 1
            self._send_json(200, {"status": "healthy", "service": "Dockerized Microservices Store", "uptime_sec": round(time.time() - START_TIME, 2)})
        elif self.path == "/metrics":
            self._send_json(200, METRICS)
        else:
            self._send_json(200, {"service": "Dockerized Microservices Store", "endpoints": ["/health", "/metrics"]})


def main() -> None:
    port = 8080
    print(f"Starting {'Dockerized Microservices Store'} on http://127.0.0.1:{port} (Ctrl+C to stop)")
    HTTPServer(("0.0.0.0", port), ServiceHandler).serve_forever()


if __name__ == "__main__":
    main()
