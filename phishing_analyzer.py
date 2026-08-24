from urllib.parse import urlparse

def analyze_url(url):
    score = 0
    reasons = []

    parsed = urlparse(url)

    if "@" in url:
        score += 2
        reasons.append("URL contains @ symbol")

    if len(url) > 75:
        score += 1
        reasons.append("URL is unusually long")

    if "-" in parsed.netloc:
        score += 1
        reasons.append("Domain contains hyphen")

    if not url.startswith("https://"):
        score += 1
        reasons.append("URL does not use HTTPS")

    if score >= 3:
        risk = "HIGH"
    elif score >= 1:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    return risk, reasons


url = input("Enter a URL: ")

risk, reasons = analyze_url(url)

print("\nRisk Level:", risk)

if reasons:
    print("Indicators found:")
    for reason in reasons:
        print("-", reason)
else:
    print("No common phishing indicators found.")
