from PIL import Image
import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


image_path = "test_image.png"  # replace with your image file


output_txt = "ocr_output.txt"

try:
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)

    if not text.strip():
        text = "[OCR succeeded but no text was detected in the image]"

    # Write text to file
    with open(output_txt, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"OCR complete! Extracted text saved to '{output_txt}'")
    print("Extracted text preview:")
    print(text)

except FileNotFoundError:
    print(f"File '{image_path}' not found!")

except Exception as e:
    print(f"OCR failed: {str(e)}")
