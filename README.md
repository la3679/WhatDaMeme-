# Meme Analyzer 🎭

![Meme Analyzer Screenshot](screenshot.png) <!-- Add a screenshot of your project here -->

Meme Analyzer is a fun and interactive web application that allows users to upload a meme image and a chat file. The application analyzes the meme using **OCR (Optical Character Recognition)** to extract text and **Google GenAI** to generate a detailed explanation of the meme, including its type, sentiment, and a humorous explanation.

---

## **Features**

- **Upload Meme Image**: Users can upload a meme image (JPG, PNG, etc.).
- **Upload Chat File**: Users can upload a chat file (TXT) to provide context for the meme.
- **Meme Analysis**:
  - Extracts text from the meme using **EasyOCR**.
  - Analyzes the meme using **Google GenAI** to determine:
    - **Meme Type**: The type of meme (e.g., "Drakeposting", "Distracted Boyfriend").
    - **Sentiment**: The overall sentiment (positive, negative, or neutral).
    - **Explanation**: A humorous and informative explanation of the meme.
- **Display Results**: The results are displayed in a user-friendly format, including the uploaded meme image.

---

## **Technologies Used**

- **Frontend**:
  - HTML, CSS, JavaScript
  - Bootstrap for styling
  - Google Fonts for typography
- **Backend**:
  - Python
  - Flask for the web server
- **Libraries**:
  - **EasyOCR**: For text extraction from images.
  - **Google GenAI**: For meme analysis and explanation.
  - **Pillow**: For image validation.
- **Other Tools**:
  - Git for version control
  - GitHub for hosting the repository

---

## **How to Run the Project**

### **Prerequisites**

1. **Python 3.x**: Ensure Python is installed on your system.
2. **Pip**: Python package manager.

### **Installation**

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/meme-analyzer.git
   cd meme-analyzer
   ```
2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up the Google GenAI API key:
   - Replace the placeholder API key in **meme_explanation.py** with your actual Google GenAI API key.
4. Run the Flask server:
   ```bash
   python app.py
   ```
5. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

### **Project Structure**

```
meme-analyzer/
├── app.py                  # Main Flask server
├── meme_explanation.py     # Meme explanation logic
├── meme_recognition.py     # Meme recognition logic
├── text_chat.py            # Chat text extraction logic
├── text_extraction.py      # OCR text extraction logic
├── requirements.txt        # List of dependencies
├── README.md               # Project documentation
├── assets/                 # Folder for uploaded files
│   ├── images/             # Folder for uploaded images
│   └── chat/               # Folder for uploaded chat files
├── templates/              # Frontend HTML files
│   └── index.html          # Main frontend file
└── uploads/                # Temporary folder for uploaded files
```

### **Results**

After uploading a meme image and a chat file, the application will display the following results:

- **Uploaded Meme Image**: The image is displayed at the top of the results section.
- **Extracted Text**: The text extracted from the meme using OCR.
- **Meme Explanation**:
  - **Meme Type**: The type of meme (e.g., "Image Comparison/Juxtaposition").
  - **Sentiment**: The overall sentiment (e.g., "Negative").
  - **Explanation**: A humorous and informative explanation of the meme.

---

## **Why We Used These Technologies**

- **Flask**: A lightweight and flexible Python web framework, perfect for small projects like this.
- **EasyOCR**: A powerful OCR library that supports multiple languages and is easy to integrate.
- **Google GenAI**: Provides advanced natural language processing capabilities for generating meme explanations.
- **Bootstrap**: Simplifies frontend development with pre-built components and responsive design.

---

## **Potential Improvements**

- **User Authentication**:
  - Add user accounts to save and track meme analysis history.
- **Meme Database**:
  - Create a database of popular memes for faster and more accurate analysis.
- **Advanced Sentiment Analysis**:
  - Use a more advanced sentiment analysis model for better accuracy.
- **Mobile App**:
  - Develop a mobile app version of the Meme Analyzer for on-the-go use.
- **Multi-Language Support**:
  - Add support for analyzing memes in multiple languages.

---

## **Screenshots**

- **Home Page**
  - Home Page <!-- Add a screenshot of the home page -->
- **Results Page**
  - Results Page <!-- Add a screenshot of the results page -->

---

## **Contributing**

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes.
4. Submit a pull request.

---

## **License**

This project is licensed under the MIT License. See the LICENSE file for details.

---

## **Acknowledgments**

- Google GenAI for providing the meme analysis API.
- EasyOCR for text extraction from images.
- Bootstrap for frontend styling.

---

## **Contact**

For questions or feedback, feel free to reach out:

- **Email**: your-email@example.com
- **GitHub**: your-username

---

### **requirements.txt**

```plaintext
Flask==2.3.2
easyocr==1.6.2
Pillow==10.0.0
google-genai==1.0.0  # Replace with the actual package name for Google GenAI
```

### **How to Use the Documentation**

- **README.md**: Explains the project scope, features, technologies used, and how to run the project. Includes screenshots and potential improvements.
- **requirements.txt**: Lists all the Python libraries required to run the project. Install them using `pip install -r requirements.txt`.
- **Screenshots**: Add screenshots of your project (e.g., home page, results page) to the README.md file.

### **Next Steps**

- Replace the placeholder API key in **meme_explanation.py** with your actual Google GenAI API key.
- Add screenshots of your project to the README.md file.
- Push the project to GitHub and share the repository link.

Let me know if you need further assistance! 🚀
