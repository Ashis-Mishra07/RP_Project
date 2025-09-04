import google.generativeai as genai
from PIL import Image
import io
import base64


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
        # Configure AI system
        genai.configure(api_key=api_key)
        
        # Initialize the model
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Create a simple prompt for text recognition
        prompt = """
        Look at this image and identify any text or words you can see. 
        Return only the text/words you can read from the image.
        If there are multiple words, return them separated by spaces.
        If you cannot see any clear text, return "No text detected".
        """
        
        # Generate response
        response = model.generate_content([prompt, image])
        
        # Extract and clean the response
        if response.text:
            recognized_text = response.text.strip()
            return recognized_text
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
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Test with a simple text prompt
        response = model.generate_content("Hello, this is a test.")
        return True if response.text else False
        
    except Exception as e:
        return False
