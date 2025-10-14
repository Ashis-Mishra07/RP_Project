"""
Direct test for handwriting recognition
"""

from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import numpy as np

def create_better_handwriting_sample():
    """Create a better handwriting sample for testing"""
    
    # Create larger image with better contrast
    img = Image.new('RGB', (800, 200), color='white')
    draw = ImageDraw.Draw(img)
    
    # Try to get a better font
    try:
        font = ImageFont.truetype("arial.ttf", 32)
    except:
        try:
            font = ImageFont.truetype("calibri.ttf", 32)
        except:
            font = ImageFont.load_default()
    
    # Draw text in blue ink color
    text = "NIT Rourkela is a good institute"
    
    # Draw with blue ink color
    draw.text((30, 80), text, fill=(0, 0, 139), font=font)  # Dark blue
    
    # Add slight variations to simulate handwriting
    # Reduce contrast slightly to simulate real handwriting
    contrast_enhancer = ImageEnhance.Contrast(img)
    img = contrast_enhancer.enhance(0.8)
    
    # Add slight blur to simulate pen ink
    img = img.filter(ImageFilter.GaussianBlur(radius=0.5))
    
    return img

def test_handwriting_recognition():
    """Test handwriting recognition with better sample"""
    
    print("🧪 Testing Handwriting Recognition")
    print("=" * 40)
    
    # Create better sample
    sample_img = create_better_handwriting_sample()
    sample_img.save('better_handwriting_sample.png')
    print("✅ Created better handwriting sample")
    
    try:
        # Test with enhanced prediction
        from predict import predict_text_from_image
        
        print("\n🔍 Testing enhanced prediction...")
        result = predict_text_from_image(sample_img)
        print(f"📝 Result: '{result}'")
        
        # Test handwriting processor directly
        print("\n🖋️  Testing handwriting processor...")
        from handwriting_processor import recognize_handwritten_text
        hw_result = recognize_handwritten_text(sample_img)
        print(f"📋 Handwriting result: '{hw_result}'")
        
        # Test enhanced OCR
        print("\n⚙️  Testing enhanced OCR...")
        from enhanced_ocr_engine import EnhancedOCREngine
        ocr = EnhancedOCREngine()
        
        is_handwriting = ocr._detect_handwriting(sample_img)
        print(f"🔍 Handwriting detected: {is_handwriting}")
        
        text, details = ocr.recognize_challenging_text(sample_img)
        print(f"📊 OCR result: '{text}'")
        print(f"🎯 Confidence: {details.get('confidence', 0):.1f}%")
        
        print(f"\n🎯 Expected: 'NIT Rourkela is a good institute'")
        print(f"✅ Best result: '{result}'")
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    from PIL import ImageFilter
    test_handwriting_recognition()