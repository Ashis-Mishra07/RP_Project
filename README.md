# Word Recognition Bot 🔍

A Python-based word recognition system that can identify and extract text from images using OCR (Optical Character Recognition).

## Features ✨

- **Image Upload**: Upload images containing text/words
- **Text Recognition**: Extract words from images using Tesseract OCR
- **Image Preprocessing**: Automatic image enhancement for better recognition
- **Multiple Modes**: Single word or multiple words/sentence recognition
- **Confidence Scores**: View OCR confidence levels
- **User-friendly Interface**: Built with Streamlit for easy interaction

## Installation 🚀

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 2. Install Tesseract OCR

**Windows:**

1. Download Tesseract from: https://github.com/UB-Mannheim/tesseract/wiki
2. Install the executable
3. Add Tesseract to your system PATH or update the path in `predict.py`

**macOS:**

```bash
brew install tesseract
```

**Linux (Ubuntu/Debian):**

```bash
sudo apt update
sudo apt install tesseract-ocr
```

## Usage 📖

### Running the Application

1. Open a terminal/command prompt
2. Navigate to the project directory
3. Run the Streamlit app:

```bash
streamlit run app.py
```

4. Open your web browser and go to `http://localhost:8501`

### Using the Interface

1. **Upload Image**: Click the file uploader and select an image with text
2. **Choose Recognition Mode**:
   - Single Word: For images with one word
   - Multiple Words/Sentence: For images with multiple words
3. **Configure Settings**: Use the sidebar to enable preprocessing view or confidence scores
4. **Recognize Text**: Click the "Recognize Text" button
5. **View Results**: See the extracted text displayed

## Project Structure 📁

```
RP/
├── app.py              # Main Streamlit application
├── preprocess.py       # Image preprocessing functions
├── predict.py          # OCR prediction functions
├── requirements.txt    # Python dependencies
├── plan.md            # Project plan and documentation
├── README.md          # This file
├── data/              # Directory for sample images
└── models/            # Directory for future ML models
```

## Technical Details 🔧

### Image Preprocessing

- Grayscale conversion
- Adaptive thresholding for binarization
- Noise removal using morphological operations
- Contrast enhancement with CLAHE

### OCR Configuration

- Uses Tesseract OCR engine
- Optimized for single word recognition (PSM 8)
- Character whitelist for better accuracy
- Confidence score calculation

## Tips for Best Results 💡

- Use clear, high-resolution images
- Ensure good contrast between text and background
- Avoid heavily stylized fonts
- Keep text horizontal (not rotated)
- Use well-lit images without shadows

## Troubleshooting 🔧

### Common Issues

1. **"Tesseract not found"**

   - Install Tesseract OCR
   - Add to system PATH
   - Update `tesseract_cmd` path in `predict.py`

2. **Poor recognition accuracy**

   - Try preprocessing the image manually
   - Ensure text is clear and readable
   - Check image resolution and quality

3. **Module import errors**
   - Install all dependencies: `pip install -r requirements.txt`
   - Check Python environment

## Future Enhancements 🚀

- Support for handwritten text recognition
- Multiple language support
- Batch processing for multiple images
- Custom ML model training
- API endpoint for integration
- Mobile app interface

## Contributing 🤝

Feel free to contribute to this project by:

- Reporting bugs
- Suggesting new features
- Submitting pull requests
- Improving documentation

## License 📄

This project is open source and available under the MIT License.
