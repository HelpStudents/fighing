#!/usr/bin/env python3

import re

def is_phishing(email_text):
    # Basic keyword-based phishing detection
    phishing_keywords = ["urgent", "bank", "password", "click", "login", "verify", "account"]
    phishing_patterns = [
        re.compile(r"click\s+here", re.IGNORECASE),
        re.compile(r"verify\s+your\s+account", re.IGNORECASE),
        re.compile(r"urgent\s+action\s+required", re.IGNORECASE),
    ]

    for keyword in phishing_keywords:
        if keyword.lower() in email_text.lower():
            return True

    for pattern in phishing_patterns:
        if pattern.search(email_text):
            return True

    return False

def main():
    email_text = input("Enter the email text: ")
    if is_phishing(email_text):
        print("Warning: This email appears to be a phishing attempt.")
    else:
        print("This email seems to be legitimate.")

if __name__ == "__main__":
    main()
