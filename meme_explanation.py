import base64
from google import genai
from google.genai import types

# Create a Google GenAI client instance with your API key.
client = genai.Client(api_key="your-api-key")  # Replace with your actual API key.

def encode_image_to_base64(image_path):
    try:
        with open(image_path, "rb") as image_file:
            encoded_bytes = base64.b64encode(image_file.read())
            encoded_str = encoded_bytes.decode("utf-8")
        return encoded_str
    except Exception as e:
        print(f"Error encoding image {image_path}: {e}")
        return ""

def explain_meme(image_path, meme_text, sentence_50):
    """
    Uses the Google GenAI SDK to analyze the meme.
    If OCR returns no text, the prompt is adjusted to include the image content
    (base64 encoded) so that the model has some visual context.
    
    Expected output format:
      Meme Type: <meme type>
      Sentiment: <sentiment>
      Explanation: <explanation>
    """
    if meme_text.strip().lower() in ["no text found", ""]:
        # Encode the image into a base64 string.
        image_b64 = encode_image_to_base64(image_path)
        prompt = f"""
        The image at '{image_path}' did not contain any readable text.
        Here is the image content as a base64 string:
        data:image/jpeg;base64,{image_b64}
        Please analyze the image and provide a detailed explanation of what is happening.
        Include:
          - The meme type (e.g., 'Drakeposting', 'Distracted Boyfriend', etc.),
          - The overall sentiment (positive, negative, or neutral),
          - And a short, funny yet informative explanation of the meme.
        Format your answer exactly as follows:
        
        Meme Type: <meme type>
        Sentiment: <sentiment>
        Explanation: <explanation>
        """
    else:
        prompt = f"""
        Analyze the following meme. The image is referenced by '{image_path}' and it contains the following text: '{meme_text}' and the converstion that happned before this meme was sent was '{sentence_50}'.
        Please provide:
          - The meme type (e.g., 'Drakeposting', 'Distracted Boyfriend', etc.),
          - The overall sentiment (positive, negative, or neutral),
          - And a short, funny yet informative explanation of the meme.
        Format your answer exactly as follows based on all the content provided:
        
        Meme Type: <meme type>
        Sentiment: <sentiment>
        Explanation: <explanation>
        """
    print("Sending prompt to Google GenAI:\n")
    
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",  # Adjust model name if necessary.
            contents=prompt,
            config=types.GenerateContentConfig(
                max_output_tokens=200,
                temperature=0.7,
            )
        )
        output = response.text  # The generated text.
        print("Received response from Google GenAI:")
        print(output)
        
        # Parse the response.
        meme_type_result = "Unknown"
        sentiment_result = "Neutral"
        explanation_result = "No explanation provided."
        for line in output.splitlines():
            if line.startswith("Meme Type:"):
                meme_type_result = line.split("Meme Type:")[1].strip()
            elif line.startswith("Sentiment:"):
                sentiment_result = line.split("Sentiment:")[1].strip()
            elif line.startswith("Explanation:"):
                explanation_result = line.split("Explanation:")[1].strip()
        return {
            "meme_type": meme_type_result,
            "sentiment": sentiment_result,
            "explanation": explanation_result
        }
    except Exception as e:
        print(f"Error during Google GenAI call: {e}")
        return {
            "meme_type": "Error",
            "sentiment": "Error",
            "explanation": f"Google GenAI error: {str(e)}"
        }
