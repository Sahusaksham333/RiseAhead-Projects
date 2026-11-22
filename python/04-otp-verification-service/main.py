"""Cryptographic 6-Digit OTP Verification Service with Expiry & Rate Limiting"""
import hmac, secrets, time

class OTPService:
    def __init__(self, ttl_seconds=120, max_attempts=3):
        self.ttl = ttl_seconds
        self.max_attempts = max_attempts
        self._store = {}

    def generate(self, user_id: str) -> str:
        code = f"{secrets.randbelow(900000) + 100000}"
        self._store[user_id] = {"code": code, "expires": time.time() + self.ttl, "attempts": 0}
        return code

    def verify(self, user_id: str, candidate: str) -> tuple[bool, str]:
        rec = self._store.get(user_id)
        if not rec: return False, "No OTP requested."
        if time.time() > rec["expires"]:
            del self._store[user_id]
            return False, "OTP expired."
        rec["attempts"] += 1
        if rec["attempts"] > self.max_attempts:
            del self._store[user_id]
            return False, "Maximum attempts exceeded."
        if hmac.compare_digest(rec["code"], candidate.strip()):
            del self._store[user_id]
            return True, "Verified successfully."
        return False, "Incorrect OTP."

if __name__ == "__main__":
    svc = OTPService()
    otp = svc.generate("user@example.com")
    print("Generated OTP:", otp)
    print("Verify result:", svc.verify("user@example.com", otp))
