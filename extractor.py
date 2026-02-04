import re

BANK_REGEX = r"\b\d{9,18}\b"
UPI_REGEX = r"\b[\w.-]+@[\w]+\b"
URL_REGEX = r"https?://[^\s]+"

def extract_intel(text: str):
    return {
        "bank_accounts": re.findall(BANK_REGEX, text),
        "upi_ids": re.findall(UPI_REGEX, text),
        "phishing_urls": re.findall(URL_REGEX, text)
    }

