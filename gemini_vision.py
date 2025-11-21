import google.generativeai as genai
from PIL import Image, ImageEnhance, ImageFilter
import io


def setup_gemini(api_key):
    """
    Setup AI system with the provided API key
    """
    try:
        genai.configure(api_key=api_key)
        return True
    except Exception as e:
        return False


def predict_with_gemini(image, api_key):
    """
    Use AI to recognize text/words from an uploaded image
    
    Args:
        image: PIL Image object
        api_key: AI API key
    
    Returns:
        str: Recognized text/words from the image
    """
    try:
        # Configure Gemini
        genai.configure(api_key=api_key)
        
        # Initialize the model
        model = genai.GenerativeModel('gemini-2.0-flash')
        
        # Specify Odia script explicitly
        prompt = """This image contains handwritten text in Odia script (ଓଡ଼ିଆ).
Extract the Odia text exactly as written.
Return only the Odia characters, nothing else."""
        
        # Generate response
        response = model.generate_content([prompt, image])
        
        if response.text:
            return response.text.strip()
        else:
            return "No text detected"
            
    except Exception as e:
        return f"Error: {str(e)}"


def test_gemini_api(api_key):
    """
    Test if the AI API key is working
    
    Args:
        api_key: AI API key
    
    Returns:
        bool: True if API is working, False otherwise
    """
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-pro')
        
        # Test with a simple text prompt
        response = model.generate_content("Hello, this is a test.")
        return True if response.text else False
        
    except Exception as e:
        return False
