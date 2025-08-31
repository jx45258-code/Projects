# Scam Analyzer

**A prototype web application to check, analyze, and report scams.**  
This project includes tools to analyze text or images for scam likelihood, lookup unknown callers, and submit scam reports.

---

## Features

- **Scam Checker**: Analyze text or images for potential scams using AI.
- **Who Just Called Me?**: Lookup numbers to see if they are reported as scams.
- **Report a Scam**: Submit scam reports via a form.
- **Informational Sections**: Guidance for victims and scam prevention.
- **Prototype UI**: Inspired by ScamShield (Singapore), includes hero banner, info sections, buttons, and AI results.

---

## Local Setup Instructions

### 1. Clone the Repository
### 2. (Optional) Create Python Environment
### 3. Install Dependencies
pip install -r requirements.txt 
install tesserect OCR from https://github.com/tesseract-ocr/tesseract?tab=readme-ov-file#running-tesseract
### 4. Configure Environment Variables
Create a .env file in the root folder with your Google API key:
GOOGLE_KEY=your_google_api_key_here
### 5. Run the Application Locally
python run.py
Open your browser at http://127.0.0.1:5000

Notes
The AI client uses Google Generative AI (google.generativeai) for scam analysis.
OCR functionality is required for image-to-text analysis.
The site is a prototype for demonstration purposes.
