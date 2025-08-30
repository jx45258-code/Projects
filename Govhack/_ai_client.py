import os
import google.generativeai as genai

_ai_client_initialized = False

def initialize_ai_client():    
    global _ai_client_initialized

    if _ai_client_initialized:
        return

    api_key = os.getenv("GOOGLE_KEY")
    if not api_key:
        raise ValueError("GOOGLE_KEY is not set in environment variables.")
    
    genai.configure(api_key=api_key)
    _ai_client_initialized = True
    print("[AI Client] Initialized successfully.")

def is_initialized() -> bool:    
    return _ai_client_initialized
