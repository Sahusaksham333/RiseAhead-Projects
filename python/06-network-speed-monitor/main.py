"""Local Throughput & Latency Benchmark Utility"""
import socket, time

def measure_tcp_latency(host="1.1.1.1", port=443, timeout=3.0) -> float:
    t0 = time.perf_counter()
    with socket.create_connection((host, port), timeout=timeout):
        return round((time.perf_counter() - t0) * 1000, 2)

def measure_loopback_throughput(mb=25) -> float:
    payload = b"x" * (1024 * 1024)
    t0 = time.perf_counter()
    buf = bytearray()
    for _ in range(mb): buf.extend(payload)
    elapsed = max(time.perf_counter() - t0, 1e-6)
    return round((mb * 8) / elapsed, 2)

if __name__ == "__main__":
    print(f"Memory/Loopback Bandwidth: {measure_loopback_throughput(20)} Mbps")
    print("Run measure_tcp_latency('google.com', 443) when online to check RTT in ms.")
