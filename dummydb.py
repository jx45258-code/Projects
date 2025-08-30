import sqlite3
from datetime import datetime

# Database file
DB_FILE = "scam_db.sqlite"

# Connect to SQLite (creates file if it doesn't exist)
conn = sqlite3.connect(DB_FILE)
c = conn.cursor()

# Create table
c.execute("""
CREATE TABLE IF NOT EXISTS scam_reports (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text_content TEXT,
    ocr_text TEXT,
    factors TEXT,
    scammer_email TEXT,
    scammer_company TEXT,
    scammer_phone TEXT,
    raw_output TEXT,
    timestamp TEXT
)
""")

# Dummy data
dummy_reports = [
    {
        "text_content": "You won $5000! Click the link to claim your prize.",
        "ocr_text": "",
        "factors": "Too-good-to-be-true offers,Urgency",
        "scammer_email": "winner@fakecasino.com",
        "scammer_company": "Fake Casino",
        "scammer_phone": "123-456-7890",
        "raw_output": "{}",
    },
    {
        "text_content": "Update your bank info immediately to avoid suspension.",
        "ocr_text": "",
        "factors": "Urgency,Request for personal info",
        "scammer_email": "security@fakemail.com",
        "scammer_company": "Fake Bank",
        "scammer_phone": "234-567-8901",
        "raw_output": "{}",
    },
    {
        "text_content": "Congratulations! You have a free iPhone waiting.",
        "ocr_text": "",
        "factors": "Too-good-to-be-true offers,Unsolicited offer",
        "scammer_email": "promo@freestuff.com",
        "scammer_company": "Free Stuff Co",
        "scammer_phone": "345-678-9012",
        "raw_output": "{}",
    },
    {
        "text_content": "Your account has been hacked. Send us your password.",
        "ocr_text": "",
        "factors": "Threatening language,Request for personal info",
        "scammer_email": "hackerman@badguy.com",
        "scammer_company": "Bad Guy Security",
        "scammer_phone": "456-789-0123",
        "raw_output": "{}",
    },
    {
        "text_content": "Limited-time investment opportunity with huge returns.",
        "ocr_text": "",
        "factors": "Too-good-to-be-true offers,Unverified links",
        "scammer_email": "invest@scamfunds.com",
        "scammer_company": "Scam Funds Inc",
        "scammer_phone": "567-890-1234",
        "raw_output": "{}",
    },
    {
        "text_content": "Claim your tax refund now by providing your SSN.",
        "ocr_text": "",
        "factors": "Request for personal info,Urgency",
        "scammer_email": "taxrefund@fakeservice.com",
        "scammer_company": "Fake Tax Service",
        "scammer_phone": "678-901-2345",
        "raw_output": "{}",
    },
    {
        "text_content": "You are selected for a $1000 gift card.",
        "ocr_text": "",
        "factors": "Unsolicited offer,Too-good-to-be-true offers",
        "scammer_email": "gift@phishing.com",
        "scammer_company": "Phish Gifts Ltd",
        "scammer_phone": "789-012-3456",
        "raw_output": "{}",
    },
    {
        "text_content": "Reset your password immediately or your account will close.",
        "ocr_text": "",
        "factors": "Threatening language,Urgency",
        "scammer_email": "support@fakecompany.com",
        "scammer_company": "Fake Company Support",
        "scammer_phone": "890-123-4567",
        "raw_output": "{}",
    },
    {
        "text_content": "Get free Bitcoin by sending 0.1 BTC first.",
        "ocr_text": "",
        "factors": "Too-good-to-be-true offers,Unverified links",
        "scammer_email": "bitcoin@scamcrypto.com",
        "scammer_company": "Scam Crypto Ltd",
        "scammer_phone": "901-234-5678",
        "raw_output": "{}",
    },
    {
        "text_content": "You've won a luxury vacation! Click to claim.",
        "ocr_text": "",
        "factors": "Too-good-to-be-true offers,Unsolicited offer",
        "scammer_email": "vacation@fakeholidays.com",
        "scammer_company": "Fake Holidays",
        "scammer_phone": "012-345-6789",
        "raw_output": "{}",
    },
]

# Insert dummy data
for report in dummy_reports:
    c.execute("""
    INSERT INTO scam_reports (text_content, ocr_text, factors, scammer_email, scammer_company, scammer_phone, raw_output, timestamp)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        report["text_content"],
        report["ocr_text"],
        report["factors"],
        report["scammer_email"],
        report["scammer_company"],
        report["scammer_phone"],
        report["raw_output"],
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

conn.commit()
conn.close()
print("Dummy scam_db.sqlite created with 10 entries.")
