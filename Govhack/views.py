import os
from flask import Blueprint, request, render_template, url_for
from werkzeug.utils import secure_filename
from .chat_service import analyze_scam

bp = Blueprint("chat", __name__)

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
UPLOAD_FOLDER = os.path.join(ROOT_DIR, "temp_uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@bp.route("/", methods=["GET", "POST"])
def chat_home():
    result = None
    report_url = None  # URL for prefilled report form

    if request.method == "POST":
        user_input = request.form.get("user_input", "")
        file = request.files.get("file_input")
        file_path = None

        if file and file.filename:
            file_path = os.path.join(UPLOAD_FOLDER, secure_filename(file.filename))
            file.save(file_path)

        result = analyze_scam(user_input, file_path=file_path)

        if file_path and os.path.exists(file_path):
            os.remove(file_path)

        if result:
            # Build URL to prefill report form
            report_url = url_for(
                "main.submit_scam_report",
                scam_type=result.get("scam_type") or "",
                scammer_contact=result.get("scammer_email") or result.get("scammer_company") or "",
                description=result.get("raw_analysis") or ""
            )

    return render_template("chat.html", result=result, report_url=report_url)

