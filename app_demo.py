import streamlit as st
from PIL import Image
import numpy as np

def main():
    """
    Demo version of Word Recognition Bot (without Tesseract dependency)
    """
    # Page configuration
    st.set_page_config(
        page_title="Word Recognition Bot - Demo",
        page_icon="🔍",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Title and description
    st.title("🔍 Word Recognition Bot - Demo Version")
    st.markdown("### Upload an image with text/words for demonstration!")
    
    # Warning about demo mode
    st.warning("📝 **Demo Mode**: This version demonstrates the interface. Install Tesseract OCR for actual word recognition.")
    
    # Sidebar for options
    with st.sidebar:
        st.header("⚙️ Settings")
        
        recognition_mode = st.selectbox(
            "Recognition Mode",
            ["Single Word", "Multiple Words/Sentence"],
            help="Choose whether to recognize a single word or multiple words/sentences"
        )
        
        show_preprocessing = st.checkbox(
            "Show Preprocessing Steps",
            value=False,
            help="Display the image preprocessing steps"
        )
        
        demo_mode = st.info("🔧 **Demo Mode Active**\n\nInstall Tesseract OCR for full functionality")
    
    # File uploader
    uploaded_file = st.file_uploader(
        "Choose an image file",
        type=['png', 'jpg', 'jpeg', 'bmp', 'tiff'],
        help="Upload an image containing text or words"
    )
    
    if uploaded_file is not None:
        # Display uploaded image
        image = Image.open(uploaded_file)
        
        # Create columns for layout
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.subheader("📷 Uploaded Image")
            st.image(image, caption="Original Image", use_column_width=True)
            
            # Show image info
            st.info(f"**Image Info:**\n- Size: {image.size}\n- Mode: {image.mode}\n- Format: {image.format}")
        
        with col2:
            st.subheader("🔍 Recognition Results")
            
            # Add a predict button
            if st.button("🚀 Recognize Text (Demo)", type="primary"):
                with st.spinner("Processing image in demo mode..."):
                    
                    # Simulate processing time
                    import time
                    time.sleep(2)
                    
                    # Demo results based on mode
                    if recognition_mode == "Single Word":
                        demo_words = ["HELLO", "WORLD", "PYTHON", "CODE", "DEMO"]
                        import random
                        predicted_text = random.choice(demo_words)
                    else:
                        demo_sentences = [
                            "Hello World",
                            "This is a demo",
                            "Word Recognition",
                            "Python OCR System",
                            "Streamlit Application"
                        ]
                        import random
                        predicted_text = random.choice(demo_sentences)
                    
                    # Display demo results
                    st.success("✅ Demo Recognition Complete!")
                    
                    # Display the recognized text in a nice format
                    st.markdown("### 📝 Demo Recognized Text:")
                    st.markdown(f"**{predicted_text}** *(Demo Result)*")
                    
                    # Demo confidence
                    st.markdown("### 📊 Demo Confidence:")
                    confidence = np.random.randint(75, 95)
                    st.progress(confidence / 100)
                    st.markdown(f"**Confidence: {confidence}%** *(Simulated)*")
                    
                    st.info("🔧 **Note**: This is a demo result. Install Tesseract OCR for actual text recognition.")
        
        # Show preprocessing steps if requested
        if show_preprocessing:
            st.subheader("🔧 Demo Preprocessing Steps")
            
            col3, col4 = st.columns([1, 1])
            
            with col3:
                st.markdown("**Original Image**")
                st.image(image, use_column_width=True)
            
            with col4:
                st.markdown("**Simulated Processed Image**")
                # Convert to grayscale for demo
                gray_image = image.convert('L')
                st.image(gray_image, use_column_width=True)
                st.caption("*Demo preprocessing (grayscale conversion)*")
    
    else:
        # Display instructions when no file is uploaded
        st.info("👆 Please upload an image to test the demo!")
        
        # Show example images or instructions
        st.markdown("### 📋 How to use this demo:")
        st.markdown("""
        1. **Upload an Image**: Click the file uploader above and select any image
        2. **Choose Mode**: Select single word or multiple words recognition mode
        3. **Click Recognize**: Press the demo recognition button
        4. **View Demo Results**: See simulated word recognition results
        """)
        
        st.markdown("### 🔧 To enable real word recognition:")
        st.markdown("""
        1. **Install Tesseract OCR** from: https://github.com/UB-Mannheim/tesseract/wiki
        2. **Restart the application**
        3. **Upload images with real text** for actual recognition
        """)
        
        # Installation button
        if st.button("📥 Download Tesseract OCR", type="primary"):
            st.balloons()
            st.success("Opening Tesseract download page...")
            st.markdown("[Click here to download Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki)")
    
    # Footer
    st.markdown("---")
    st.markdown("🚀 **Demo Mode** - Made with ❤️ using Streamlit | Install Tesseract OCR for full functionality")


if __name__ == "__main__":
    main()
