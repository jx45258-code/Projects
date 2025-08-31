from flask import request, render_template, redirect, url_for, flash, Blueprint
from collections import Counter
import sqlite3
import os


main_bp = Blueprint("main", __name__)
DB_PATH = os.path.join(os.path.dirname(__file__), "static", "db", "fake_callers.db")
REPORT_DB = os.path.join(os.path.dirname(__file__), "static", "db", "report_scams.db")

@main_bp.route("/")
def home():
    return render_template("home.html")

@main_bp.route("/privacy")
def privacy():
    return render_template("privacy.html")

@main_bp.route("/terms")
def terms():
    return render_template("terms.html")


@main_bp.route("/who-called", methods=["GET", "POST"])
def who_called():
    search_query = request.form.get("search_number", "").strip()
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    
    if search_query:
        c.execute("SELECT * FROM callers WHERE phone_number LIKE ?", (f"%{search_query}%",))
    else:
        c.execute("SELECT * FROM callers")
    
    rows = c.fetchall()
    conn.close()
    
    
    phone_counts = Counter(row['phone_number'] for row in rows)
    
    
    grouped = {}
    for row in rows:
        phone = row['phone_number']
        if phone not in grouped:
            grouped[phone] = {
                "name": row['name'],
                "phone_number": phone,
                "company": row['company'],
                "call_type": row['call_type'],
                "notes": row['notes'],
                "reports": phone_counts[phone]
            }
    
    callers = list(grouped.values())
    
    return render_template("report.html", callers=callers, search_query=search_query)



@main_bp.route("/report-scam", methods=["GET", "POST"])
def submit_scam_report():
  
    prefill = {
        "scam_type": request.args.get("scam_type", ""),
        "scammer_contact": request.args.get("scammer_contact", ""),
        "description": request.args.get("description", "")
    }

    if request.method == "POST":
        scam_type = request.form.get("scam_type", "").strip()
        scammer_contact = request.form.get("scammer_contact", "").strip()
        financial_loss = request.form.get("financial_loss", "").strip()
        reporter_email = request.form.get("reporter_email", "").strip()
        description = request.form.get("description", "").strip()

       
        conn = sqlite3.connect(REPORT_DB)
        c = conn.cursor()
        c.execute('''
            INSERT INTO reports (scam_type, scammer_contact, financial_loss, reporter_email, description)
            VALUES (?, ?, ?, ?, ?)
        ''', (scam_type, scammer_contact, financial_loss, reporter_email, description))
        conn.commit()
        conn.close()

        flash("Your report has been submitted!", "success")
        return render_template("report_success.html")

    return render_template("report_scam.html", prefill=prefill)


@main_bp.route("/been-scammed")
def been_scammed():
    return render_template("scammed.html")

@main_bp.route("/real-or-fake")
def realorfake():
    return render_template("realorfake.html")