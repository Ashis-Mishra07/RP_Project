import cv2
import numpy as np
from PIL import Image


def preprocess_image(image_path):
    """
    Preprocess an uploaded image for word recognition.
    
    Args:
        image_path (str): Path to the input image
        
    Returns:
        numpy.ndarray: Preprocessed image ready for OCR
    """
    # Load the image
    img = cv2.imread(image_path)
    
    if img is None:
        raise ValueError("Could not load image. Please check the file path.")
    
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply thresholding (binarization)
    # Using adaptive threshold for better results with varying lighting
    thresh = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
    )
    
    # Remove noise using morphological operations
    kernel = np.ones((2, 2), np.uint8)
    
    # Opening (erosion followed by dilation) removes noise
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
    
    # Closing (dilation followed by erosion) fills holes
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel, iterations=1)
    
    return closing


def preprocess_pil_image(pil_image):
    """
    Preprocess a PIL Image object for word recognition.
    
    Args:
        pil_image (PIL.Image): PIL Image object
        
    Returns:
        numpy.ndarray: Preprocessed image ready for OCR
    """
    # Convert PIL image to numpy array
    img_array = np.array(pil_image)
    
    # If image is RGB, convert to BGR for OpenCV
    if len(img_array.shape) == 3 and img_array.shape[2] == 3:
        img_array = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
    
    # Convert to grayscale if not already
    if len(img_array.shape) == 3:
        gray = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)
    else:
        gray = img_array
    
    # Apply thresholding (binarization)
    thresh = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
    )
    
    # Remove noise using morphological operations
    kernel = np.ones((2, 2), np.uint8)
    
    # Opening removes noise
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
    
    # Closing fills holes
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel, iterations=1)
    
    return closing


def resize_image(image, target_height=64):
    """
    Resize image while maintaining aspect ratio.
    
    Args:
        image (numpy.ndarray): Input image
        target_height (int): Target height for the resized image
        
    Returns:
        numpy.ndarray: Resized image
    """
    height, width = image.shape[:2]
    
    # Calculate new width maintaining aspect ratio
    aspect_ratio = width / height
    target_width = int(target_height * aspect_ratio)
    
    # Resize the image
    resized = cv2.resize(image, (target_width, target_height), interpolation=cv2.INTER_AREA)
    
    return resized


def enhance_contrast(image):
    """
    Enhance contrast of the image using CLAHE (Contrast Limited Adaptive Histogram Equalization).
    
    Args:
        image (numpy.ndarray): Input grayscale image
        
    Returns:
        numpy.ndarray: Enhanced image
    """
    # Create CLAHE object
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    
    # Apply CLAHE
    enhanced = clahe.apply(image)
    
    return enhanced
