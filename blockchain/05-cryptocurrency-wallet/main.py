#!/usr/bin/env python3
"""
Cryptocurrency Wallet — RiseAhead Blockchain & Cryptographic Ledger Simulator
Study UTXO transaction signing, key derivation, and peer-to-peer consensus.

Pure Python 3 SHA-256 Proof-of-Work blockchain ledger with chain integrity verification.
"""
import hashlib
import json
import time


class Block:
    def __init__(self, index: int, data: dict, prev_hash: str) -> None:
        self.index = index
        self.timestamp = round(time.time(), 3)
        self.data = data
        self.prev_hash = prev_hash
        self.nonce = 0
        self.hash = self.mine(difficulty=2)

    def compute_hash(self) -> str:
        payload = json.dumps(
            {"index": self.index, "timestamp": self.timestamp, "data": self.data, "prev_hash": self.prev_hash, "nonce": self.nonce},
            sort_keys=True,
        ).encode()
        return hashlib.sha256(payload).hexdigest()

    def mine(self, difficulty: int = 2) -> str:
        prefix = "0" * difficulty
        while True:
            h = self.compute_hash()
            if h.startswith(prefix):
                return h
            self.nonce += 1


class Ledger:
    def __init__(self) -> None:
        self.chain = [Block(0, {"event": "GENESIS", "app": "Cryptocurrency Wallet"}, "0" * 64)]

    def add_record(self, data: dict) -> Block:
        blk = Block(len(self.chain), data, self.chain[-1].hash)
        self.chain.append(blk)
        return blk

    def is_valid(self) -> bool:
        for i in range(1, len(self.chain)):
            cur, prev = self.chain[i], self.chain[i - 1]
            if cur.prev_hash != prev.hash or cur.hash != cur.compute_hash():
                return False
        return True


def main() -> None:
    print("=" * 64)
    print(f"RiseAhead Blockchain Engine: Cryptocurrency Wallet")
    print("=" * 64)
    ledger = Ledger()
    ledger.add_record({"actor": "alice", "action": "submit", "value": 100})
    ledger.add_record({"actor": "bob", "action": "verify", "value": 100})
    for b in ledger.chain:
        print(f"Block #{b.index} | nonce={b.nonce:4d} | hash={b.hash[:18]}... | data={b.data}")
    print(f"\nChain Integrity Verified: {ledger.is_valid()}")


if __name__ == "__main__":
    main()
