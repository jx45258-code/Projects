import os
import json
import pytesseract
from PIL import Image
import google.generativeai as genai
from ._ai_client import is_initialized, initialize_ai_client

# Tesseract (Windows)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PROMPTS_JSON_PATH = os.path.join(ROOT_DIR, "files", "prompts.json")

def default_result(ocr_text="", ai_output=""):
    return {
        "score": 0, "factors": [], "raw_analysis": "", "ocr_text": ocr_text,
        "scammer_email": None, "scammer_company": None, "scammer_phone": None,
        "scam_type": None, "raw_output": ai_output
    }

def load_prompt(template_name, user_input):
    try:
        with open(PROMPTS_JSON_PATH, "r", encoding="utf-8") as f:
            prompts = json.load(f)
        template = prompts[template_name]["template"]
        return template.replace("{user_input}", user_input)
    except Exception as e:
        print(f"[prompts] failed: {e} | tried: {PROMPTS_JSON_PATH}")
        return user_input

def extract_text_from_image(file_path):
    try:
        with Image.open(file_path) as img:
            return pytesseract.image_to_string(img)
    except Exception as e:
        print(f"OCR failed: {e}")
        return ""

def clean_ai_json_output(ai_output: str) -> str:
    """
    Remove Markdown code block wrappers from AI output before JSON parsing.
    """
    ai_output = ai_output.strip()
    if ai_output.startswith("```") and ai_output.endswith("```"):
        # Strip the triple backticks
        content = ai_output[3:-3].strip()
        # Remove optional 'json' tag at the start
        if content.lower().startswith("json"):
            content = "\n".join(content.splitlines()[1:]).strip()
        return content
    return ai_output


def analyze_scam(user_input="", file_path=None):
    # Ensure AI client is initialized
    if not is_initialized():
        try:
            initialize_ai_client()
        except Exception as e:
            print(f"[AI Client] Initialization failed: {e}")
            return default_result()

    ocr_text = extract_text_from_image(file_path) if file_path and os.path.exists(file_path) else ""
    text_to_analyze = (user_input or "").strip()
    if ocr_text:
        text_to_analyze += ("\n" + ocr_text.strip()) if text_to_analyze else ocr_text.strip()
    if not text_to_analyze:
        return default_result(ocr_text=ocr_text)

    ocr_notice = ("Note: The text may have been extracted from an image using OCR. "
                  "Minor spelling, grammar, or formatting errors should not be counted as suspicious. "
                  "Focus only on clear content-based indicators of scams.\n\n") if ocr_text else ""

    prompt = ocr_notice + load_prompt("basic", text_to_analyze)

    ai_output = ""
    try:
        model = genai.GenerativeModel("gemini-2.0-flash-lite")
        response = model.generate_content(prompt)
        ai_output = response.text or ""
        print("AI raw output:", repr(ai_output))
    except Exception as e:
        print(f"Gemini call failed: {e}")
        return default_result(ocr_text=ocr_text, ai_output=ai_output)

    # Clean AI output from Markdown code block wrappers
    ai_text = clean_ai_json_output(ai_output)

    try:
        parsed = json.loads(ai_text)
    except Exception as e:
        print(f"JSON parse failed: {e}")
        parsed = {
            "score": 0,
            "factors": [],
            "raw_analysis": ai_text or "No AI output",
            "scammer_email": None,
            "scammer_company": None,
            "scammer_phone": None,
            "scam_type": None
        }

    return {
        "score": parsed.get("score", 0),
        "factors": parsed.get("factors", []),
        "raw_analysis": parsed.get("raw_analysis", ai_text),
        "ocr_text": ocr_text,
        "scammer_email": parsed.get("scammer_email"),
        "scammer_company": parsed.get("scammer_company"),
        "scammer_phone": parsed.get("scammer_phone"),
        "scam_type": parsed.get("scam_type"),
        "raw_output": ai_output,
    }
