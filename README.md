Scam Analyzer – Local Setup Instructions
Project Overview

This Flask project allows users to check if a message or image is a scam. Key features include:

Text Analysis – Paste text or upload an image for AI scam detection.

Image OCR – Extract text from uploaded images using Tesseract OCR.

Caller Database Lookup – Search for suspicious phone numbers.

Reporting – Submit a scam report through the system.

Prerequisites

Python 3.11+ installed.

Git for cloning the repository.

Tesseract OCR installed and accessible in your PATH.

Windows: Download Tesseract installer
 and ensure tesseract.exe is in PATH.

macOS: brew install tesseract

Linux (Ubuntu/Debian): sudo apt install tesseract-ocr

Setup Instructions
1. Clone the repository
git clone <your-repo-url>
cd <your-repo-folder>

2. Create a virtual environment
python -m venv venv

3. Activate the environment

Windows: venv\Scripts\activate

macOS/Linux: source venv/bin/activate

4. Install dependencies
pip install -r requirements.txt


Required packages include:

Flask

google-generativeai

Pillow

pytesseract

5. Set up environment variables

Create a .env file in the root folder:

GOOGLE_KEY=<your-google-generative-ai-key>

6. Verify Tesseract installation

Run the following in Python:

import pytesseract
pytesseract.get_tesseract_version()


You should see the version number.

Running the Application Locally
python run.py


Open your browser at: http://127.0.0.1:5000

Upload a screenshot or paste scam text to test.

Folder Structure (Current)
project/
│
├── Govhack/                # Flask application package
│   ├── __init__.py
│   ├── routes.py
│   ├── static/
│   │   ├── css/
│   │   ├── images/
│   │   └── db/
│   └── templates/
│       ├── home.html
│       ├── chat.html
│       ├── report_scam.html
│       └── ...
├── run.py
├── .env
└── requirements.txt

Notes

OCR is required for image analysis; ensure Tesseract is installed.

The AI client will only initialize once per session.

Make sure your .env file is correctly loaded before running.
