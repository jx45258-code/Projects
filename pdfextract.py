import PyPDF2
from pathlib import Path

PDF_FILE = Path("lbs.pdf")
TXT_FILE = Path("lbs.txt")

def pdf_to_txt(pdf_path, txt_path):
    text = ""
    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"Converted {pdf_path} ? {txt_path}")

if __name__ == "__main__":
    if not PDF_FILE.exists():
        print(f"File {PDF_FILE} does not exist.")
    else:
        pdf_to_txt(PDF_FILE, TXT_FILE)
