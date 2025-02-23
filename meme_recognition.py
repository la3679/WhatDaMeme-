import os
from PIL import Image
from text_extraction import extract_text
from meme_explanation import explain_meme
from text_chat import get_last_50_sentences_efficient

def is_image_file(image_path):
    print(f"Verifying if '{image_path}' is a valid image...")
    try:
        with Image.open(image_path) as img:
            img.verify()  # Check if the image is valid.
        print("Image verification successful.")
        return True
    except Exception as e:
        print(f"Image verification failed for '{image_path}': {e}")
        return False

def process_meme(image_path):
    print(f"\nStarting process_meme for '{image_path}'")
    
    # Step 1: Validate that the file is an image.
    if not is_image_file(image_path):
        print("Not a valid image. Exiting process_meme.")
        return {"error": "File is not a valid image."}
    
    # Step 2: Extract text from the image using OCR.
    print("Extracting text using OCR...")
    meme_text = extract_text(image_path)
    print(f"Extracted text: {meme_text}")
    
    # Step 3: Get text from text chat.
    last_50 = get_last_50_sentences_efficient('assets/chat/myfile.txt')
    sentence_50 = " ".join(last_50)
    
    # Step 4: Get explanation from Google GenAI.
    print("Generating meme explanation using Google GenAI...")
    explanation_data = explain_meme(image_path, meme_text, sentence_50)
    
    print("process_meme complete, returning results.")
    return {
        "extracted_text": meme_text,
        "meme_explanation": explanation_data
    }