import easyocr

print("Initializing EasyOCR reader...")
reader = easyocr.Reader(["en"])
print("EasyOCR reader initialized successfully.")

def extract_text(image_path):
    print(f"Starting OCR extraction for '{image_path}'")
    try:
        results = reader.readtext(image_path, detail=0)
        extracted = " ".join(results) if results else "No text found"
        print(f"OCR extraction complete for '{image_path}'")
        return extracted
    except Exception as e:
        error_message = f"Error during OCR: {str(e)}"
        print(error_message)
        return error_message
