import os
from flask import Blueprint, request, render_template
from werkzeug.utils import secure_filename
from .chat_service import analyze_scam

bp = Blueprint("chat", __name__)

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
UPLOAD_FOLDER = os.path.join(ROOT_DIR, "temp_uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@bp.route("/", methods=["GET", "POST"])
def chat_home():
    result = None
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

        # if you want JSON fetch style, return jsonify(result) instead
    return render_template("chat.html", result=result)
