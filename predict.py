import pytesseract
import cv2
import numpy as np
from preprocess import preprocess_image, preprocess_pil_image
import re


# Configure Tesseract path (update this path based on your Tesseract installation)
# For Windows, typically: r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def predict_word_from_path(image_path):
    """
    Predict word from an image file path using OCR.
    
    Args:
        image_path (str): Path to the image file
        
    Returns:
        str: Predicted word(s) from the image
    """
    try:
        # Preprocess the image
        processed_image = preprocess_image(image_path)
        
        # Use Tesseract to extract text
        # Using PSM 8 for single word recognition
        custom_config = r'--oem 3 --psm 8 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        
        text = pytesseract.image_to_string(processed_image, config=custom_config)
        
        # Clean the extracted text
        cleaned_text = clean_text(text)
        
        return cleaned_text
        
    except Exception as e:
        return f"Error processing image: {str(e)}"


def predict_word_from_pil(pil_image):
    """
    Predict word from a PIL Image object using OCR.
    
    Args:
        pil_image (PIL.Image): PIL Image object
        
    Returns:
        str: Predicted word(s) from the image
    """
    try:
        # Preprocess the PIL image
        processed_image = preprocess_pil_image(pil_image)
        
        # Use Tesseract to extract text
        # Using PSM 8 for single word recognition
        custom_config = r'--oem 3 --psm 8 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        
        text = pytesseract.image_to_string(processed_image, config=custom_config)
        
        # Clean the extracted text
        cleaned_text = clean_text(text)
        
        return cleaned_text
        
    except Exception as e:
        return f"Error processing image: {str(e)}"


def predict_multiple_words(pil_image):
    """
    Predict multiple words from an image (for sentences or multiple words).
    
    Args:
        pil_image (PIL.Image): PIL Image object
        
    Returns:
        str: Predicted text from the image
    """
    try:
        # Preprocess the PIL image
        processed_image = preprocess_pil_image(pil_image)
        
        # Use Tesseract to extract text
        # Using PSM 6 for uniform block of text
        custom_config = r'--oem 3 --psm 6'
        
        text = pytesseract.image_to_string(processed_image, config=custom_config)
        
        # Clean the extracted text
        cleaned_text = clean_text(text)
        
        return cleaned_text
        
    except Exception as e:
        return f"Error processing image: {str(e)}"


def clean_text(text):
    """
    Clean and format the extracted text.
    
    Args:
        text (str): Raw text from OCR
        
    Returns:
        str: Cleaned text
    """
    # Remove extra whitespace and newlines
    text = text.strip()
    
    # Remove non-alphabetic characters (keeping spaces for multiple words)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text)
    
    # Return the cleaned text
    return text.strip() if text.strip() else "No text detected"


def get_confidence_score(pil_image):
    """
    Get confidence scores for the OCR prediction.
    
    Args:
        pil_image (PIL.Image): PIL Image object
        
    Returns:
        dict: Dictionary containing text and confidence information
    """
    try:
        # Preprocess the PIL image
        processed_image = preprocess_pil_image(pil_image)
        
        # Get detailed data including confidence scores
        data = pytesseract.image_to_data(processed_image, output_type=pytesseract.Output.DICT)
        
        # Extract words with confidence > 0
        words_with_confidence = []
        for i, word in enumerate(data['text']):
            if int(data['conf'][i]) > 0:
                words_with_confidence.append({
                    'word': word,
                    'confidence': int(data['conf'][i])
                })
        
        return {
            'words': words_with_confidence,
            'average_confidence': np.mean([w['confidence'] for w in words_with_confidence]) if words_with_confidence else 0
        }
        
    except Exception as e:
        return {'error': f"Error getting confidence scores: {str(e)}"}


def check_tesseract_installation():
    """
    Check if Tesseract is properly installed and accessible.
    
    Returns:
        bool: True if Tesseract is working, False otherwise
    """
    try:
        # Try to get Tesseract version
        version = pytesseract.get_tesseract_version()
        print(f"Tesseract version: {version}")
        return True
    except Exception as e:
        print(f"Tesseract not found or not working: {str(e)}")
        print("Please install Tesseract OCR:")
        print("Windows: Download from https://github.com/UB-Mannheim/tesseract/wiki")
        print("Make sure to add Tesseract to your system PATH or update the tesseract_cmd path in this file.")
        return False
