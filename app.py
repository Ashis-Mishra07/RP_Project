import streamlit as st
from PIL import Image
from vision_agent import vision_agent
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def main():
    """
    Advanced Vision-Language Agent for Text Recognition
    """
    # Page configuration
    st.set_page_config(
        page_title="VisionText Agent",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Title and description
    st.title("🤖 VisionText Agent")
    st.markdown("### Advanced Multi-Stage Text Recognition System")
    st.markdown("*Powered by Vision Transformer and Multi-Modal AI Architecture*")
    
    # Sidebar for agent status
    with st.sidebar:
        st.header("🔧 Agent System")
        
        # Get agent info
        agent_info = vision_agent.get_agent_info()
        
        # Test agent system
        with st.spinner("Testing Agent System..."):
            is_ready, status_msg = vision_agent.test_agent_system()
            if is_ready:
                st.success("✅ Agent System Operational!")
                st.info(f"🤖 {agent_info['agent_name']} v{agent_info['version']}")
            else:
                st.error(f"❌ {status_msg}")
        
        # Show agent components
        st.markdown("### 🧠 Agent Components:")
        for i, stage in enumerate(agent_info['processing_pipeline'], 1):
            st.markdown(f"**{i}.** {stage}")
        
        # Performance metrics
        st.markdown("### 📊 Performance:")
        perf = agent_info['performance']
        st.metric("Accuracy", perf['accuracy'])
        st.metric("Speed", perf['speed'])
        st.metric("Languages", perf['languages'])
    
    # File uploader
    uploaded_file = st.file_uploader(
        "Choose an image file",
        type=['png', 'jpg', 'jpeg', 'bmp', 'tiff'],
        help="Upload an image containing text or words"
    )
    
    if uploaded_file is not None:
        # Display uploaded image
        image = Image.open(uploaded_file)
        
        # Show a compact preview of the uploaded image first
        st.markdown("### 📷 Uploaded Image Preview")
        
        # Create a container for the image preview
        img_container = st.container()
        with img_container:
            # Create columns for better layout - smaller image column
            img_col, space_col, info_col = st.columns([2, 0.5, 3])
            
            with img_col:
                # Display image in a smaller, rectangular format
                st.image(
                    image, 
                    caption="Your uploaded image",
                    width=300,  # Fixed width for consistent sizing
                    use_column_width=False
                )
                
                # Show basic image info
                st.caption(f"📊 Size: {image.size[0]} x {image.size[1]} pixels")
                st.caption(f"📁 Format: {image.format}")
            
            with info_col:
                st.markdown("### 🔍 Agent Processing")
                
                # Check if agent is ready
                if vision_agent.is_ready:
                    # Add a process button
                    if st.button("🚀 Start Agent Processing", type="primary", use_container_width=True):
                        
                        # Create containers for real-time progress
                        progress_container = st.container()
                        result_container = st.container()
                        
                        with progress_container:
                            # Progress bar and status
                            progress_bar = st.progress(0)
                            status_text = st.empty()
                            
                            # Stage details container
                            stage_details = st.expander("🔍 View Processing Stages", expanded=True)
                            
                            def update_progress(stage_msg, progress):
                                progress_bar.progress(progress / 100)
                                status_text.text(f"🤖 Agent Status: {stage_msg}")
                                with stage_details:
                                    st.write(f"⚙️ {stage_msg}")
                            
                            # Process with agent
                            predicted_text, stage_results = vision_agent.process_image_with_agent(
                                image, 
                                progress_callback=update_progress
                            )
                            
                            # Clear progress when done
                            progress_bar.progress(100)
                            status_text.text("✅ Agent processing complete!")
                        
                        with result_container:
                            # Display results
                            if predicted_text and predicted_text != "No text detected" and not predicted_text.startswith("Error"):
                                st.success("✅ Agent Recognition Complete!")
                                
                                # Add some spacing
                                st.markdown("---")
                                
                                # Display the recognized text with better formatting
                                st.markdown("## 📝 Agent Recognition Result")
                                
                                # Create a highlighted box for the result
                                st.markdown(
                                    f"""
                                    <div style="
                                        background-color: #f0f2f6;
                                        padding: 20px;
                                        border-radius: 10px;
                                        border-left: 5px solid #4CAF50;
                                        margin: 15px 0;
                                    ">
                                        <h3 style="color: #1f1f1f; margin-bottom: 10px;">🤖 Agent Detected Text:</h3>
                                        <h2 style="color: #2E86AB; font-weight: bold; font-size: 28px; margin: 0;">
                                            {predicted_text}
                                        </h2>
                                    </div>
                                    """, 
                                    unsafe_allow_html=True
                                )
                                
                                # Show agent processing details
                                with st.expander("📊 Agent Processing Details"):
                                    col_a, col_b = st.columns(2)
                                    
                                    with col_a:
                                        st.markdown("**Preprocessing Results:**")
                                        if "preprocessing" in stage_results:
                                            prep = stage_results["preprocessing"]
                                            st.text(f"Original Size: {prep['original_size']}")
                                            st.text(f"Format: {prep['format']}")
                                            st.text(f"Status: {prep['status']}")
                                    
                                    with col_b:
                                        st.markdown("**Post-processing Results:**")
                                        if "post_processing" in stage_results:
                                            post = stage_results["post_processing"]
                                            st.text(f"Confidence: {post['confidence_score']}")
                                            st.text(f"Language: {post['language_detected']}")
                                            st.text(f"Status: {post['status']}")
                                
                                # Store result in session state
                                st.session_state.last_result = predicted_text
                                
                            else:
                                if predicted_text.startswith("Error"):
                                    st.error(f"❌ Agent Error: {predicted_text}")
                                else:
                                    st.warning("⚠️ Agent could not detect any text in the image.")
                                    
                                    # Add spacing
                                    st.markdown("---")
                                    
                                    # Display no detection message with better formatting
                                    st.markdown(
                                        """
                                        <div style="
                                            background-color: #fff3cd;
                                            padding: 20px;
                                            border-radius: 10px;
                                            border-left: 5px solid #ffc107;
                                            margin: 15px 0;
                                        ">
                                            <h3 style="color: #856404; margin-bottom: 10px;">🤖 Agent Detection Result:</h3>
                                            <h2 style="color: #856404; font-weight: bold; font-size: 24px; margin: 0;">
                                                No text detected by agent
                                            </h2>
                                        </div>
                                        """, 
                                        unsafe_allow_html=True
                                    )
                                    
                                    st.markdown("### 💡 Agent Optimization Tips:")
                                    st.markdown("""
                                    - Ensure the text is clear and readable
                                    - Try images with good contrast
                                    - Avoid blurry or low-resolution images
                                    - Make sure the text is not too small
                                    """)
                else:
                    st.error("❌ Agent system not ready. Please check configuration!")
    
    else:
        # Display instructions when no file is uploaded
        st.info("👆 Please upload an image to start agent processing!")
        
        # Show agent architecture information
        st.markdown("### 🤖 VisionText Agent Architecture:")
        
        agent_info = vision_agent.get_agent_info()
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**🧠 Multi-Stage Processing Pipeline:**")
            for i, stage in enumerate(agent_info['processing_pipeline'], 1):
                st.markdown(f"**Stage {i}:** {stage}")
        
        with col2:
            st.markdown("**🔧 Models & Algorithms:**")
            for model in agent_info['models_used']:
                st.markdown(f"• {model}")
        
        st.markdown("### 📊 Agent Performance Metrics:")
        perf_col1, perf_col2, perf_col3 = st.columns(3)
        
        with perf_col1:
            st.metric("🎯 Accuracy", agent_info['performance']['accuracy'])
        
        with perf_col2:
            st.metric("⚡ Processing Speed", agent_info['performance']['speed'])
        
        with perf_col3:
            st.metric("🌍 Language Support", agent_info['performance']['languages'])
    
    # Footer
    st.markdown("---")
    st.markdown("**VisionText Agent** - *Powered by Advanced Vision-Language Architecture*")


if __name__ == "__main__":
    main()
