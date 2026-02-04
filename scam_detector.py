SCAM_KEYWORDS = [
    "kyc", "account blocked", "urgent",
    "verify", "click", "link",
    "upi", "bank", "otp"
]

def detect_scam(text: str):
    text = text.lower()
    hits = sum(1 for k in SCAM_KEYWORDS if k in text)

    return {
        "is_scam": hits >= 2,
        "confidence": min(0.3 + hits * 0.15, 0.99),
        "scam_type": "phishing" if hits >= 2 else "unknown"
    }

