from flask import Flask, request, jsonify, render_template
import os
from meme_recognition import process_meme

app = Flask(__name__)

# Ensure the uploads directory exists
os.makedirs('uploads', exist_ok=True)
os.makedirs('assets/images', exist_ok=True)
os.makedirs('assets/chat', exist_ok=True)

# Route to serve the frontend
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle meme processing
@app.route('/process_meme', methods=['POST'])
def process_meme_route():
    if 'image' not in request.files or 'chat' not in request.files:
        return jsonify({"error": "Both image and chat files are required"}), 400
    
    image_file = request.files['image']
    chat_file = request.files['chat']
    
    if image_file.filename == '' or chat_file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    # Save the files temporarily
    image_path = os.path.join('uploads', image_file.filename)
    chat_path = os.path.join('uploads', chat_file.filename)
    image_file.save(image_path)
    chat_file.save(chat_path)
    
    # Move the chat file to the assets/chat folder
    final_chat_path = os.path.join('assets/chat', 'myfile.txt')
    os.replace(chat_path, final_chat_path)
    
    # Process the meme
    result = process_meme(image_path)
    
    # Clean up the uploaded image file
    os.remove(image_path)
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)