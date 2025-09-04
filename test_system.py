"""
Test script to verify the word recognition system components
"""

def test_imports():
    """Test if all required modules can be imported"""
    try:
        import cv2
        print("✅ OpenCV imported successfully")
    except ImportError as e:
        print(f"❌ OpenCV import failed: {e}")
    
    try:
        import numpy as np
        print("✅ NumPy imported successfully")
    except ImportError as e:
        print(f"❌ NumPy import failed: {e}")
    
    try:
        from PIL import Image
        print("✅ Pillow imported successfully")
    except ImportError as e:
        print(f"❌ Pillow import failed: {e}")
    
    try:
        import pytesseract
        print("✅ PyTesseract imported successfully")
    except ImportError as e:
        print(f"❌ PyTesseract import failed: {e}")
    
    try:
        import streamlit as st
        print("✅ Streamlit imported successfully")
    except ImportError as e:
        print(f"❌ Streamlit import failed: {e}")


def test_modules():
    """Test our custom modules"""
    try:
        from preprocess import preprocess_pil_image
        print("✅ Preprocess module imported successfully")
    except ImportError as e:
        print(f"❌ Preprocess module import failed: {e}")
    
    try:
        from predict import predict_word_from_pil, check_tesseract_installation
        print("✅ Predict module imported successfully")
        
        # Test Tesseract installation
        print("\n🔍 Checking Tesseract installation...")
        if check_tesseract_installation():
            print("✅ Tesseract is working properly")
        else:
            print("❌ Tesseract is not working - please install it")
            
    except ImportError as e:
        print(f"❌ Predict module import failed: {e}")


if __name__ == "__main__":
    print("🧪 Testing Word Recognition System Components\n")
    print("=" * 50)
    
    print("\n1. Testing Library Imports:")
    test_imports()
    
    print("\n2. Testing Custom Modules:")
    test_modules()
    
    print("\n" + "=" * 50)
    print("🎯 Test Complete!")
    print("\nIf all imports are successful, you can run the app with:")
    print("streamlit run app.py")
