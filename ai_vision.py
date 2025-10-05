import google.generativeai as genai
from PIL import Image
import io
import base64
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def setup_ai():
    """
    Setup Model system with the API key from environment
    """
    try:
        api_key = os.getenv('MODEL_API_KEY')
        if not api_key:
            return False
        genai.configure(api_key=api_key)
        return True
    except Exception as e:
        return False


def predict_with_ai(image):
    """
    Use Model to recognize text/words from an uploaded image
    
    Args:
        image: PIL Image object
    
    Returns:
        str: Recognized text/words from the image
    """
    try:
        # Get API key from environment
        api_key = os.getenv('MODEL_API_KEY')
        if not api_key:
            return "Error: Model API key not found in environment"
            
        # Configure Model system
        genai.configure(api_key=api_key)
        
        # Initialize the model
        model_name = os.getenv('MODEL_NAME_VISION', 'gemini-pro-vision')
        model = genai.GenerativeModel(model_name)
        
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


def test_ai_api():
    """
    Test if the Model API key is working
    
    Returns:
        bool: True if API is working, False otherwise
    """
    try:
        # Get API key from environment
        api_key = os.getenv('MODEL_API_KEY')
        if not api_key:
            return False
            
        genai.configure(api_key=api_key)
        model_name = os.getenv('MODEL_NAME_TEXT', 'gemini-pro')
        model = genai.GenerativeModel(model_name)
        
        # Test with a simple text prompt
        response = model.generate_content("Hello, this is a test.")
        return True if response.text else False
        
    except Exception as e:
        return False
