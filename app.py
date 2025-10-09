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
                    use_container_width=False
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
                                
                                # Show detailed stage-by-stage results
                                st.markdown("## 🔬 Detailed Stage Analysis")
                                
                                for stage_num in range(1, 7):
                                    stage_key = f"stage_{stage_num}"
                                    if stage_key in stage_results:
                                        stage_info = stage_results[stage_key]
                                        
                                        with st.expander(f"📊 {stage_info['name']} - {stage_info['status']}", expanded=False):
                                            
                                            # Special handling for different stages
                                            if stage_num == 1:  # Image Preprocessing
                                                col_left, col_right = st.columns([1, 1])
                                                with col_left:
                                                    st.markdown("**Input:**")
                                                    st.info(stage_info['input'])
                                                    if 'result_image' in stage_info and stage_info['result_image']:
                                                        st.markdown("**Original Image:**")
                                                        st.image(image, caption="Original Image", width=250)
                                                
                                                with col_right:
                                                    st.markdown("**Output:**")
                                                    st.success(stage_info['output'])
                                                    if 'result_image' in stage_info and stage_info['result_image']:
                                                        st.markdown("**Enhanced Image:**")
                                                        st.image(stage_info['result_image'], caption="After Enhancement", width=250)
                                            
                                            elif stage_num == 2:  # Feature Extraction - Fix layout
                                                st.markdown("**Input:**")
                                                st.info(stage_info['input'])
                                                st.markdown("**Output:**")
                                                st.success(stage_info['output'])
                                                
                                                if 'result_data' in stage_info and stage_info['result_data']:
                                                    col1, col2 = st.columns(2)
                                                    
                                                    with col1:
                                                        st.markdown("**🔍 Patch Analysis:**")
                                                        patch_data = stage_info['result_data'].get('patch_analysis', {})
                                                        for key, value in patch_data.items():
                                                            st.text(f"{key.replace('_', ' ').title()}: {value}")
                                                        
                                                        st.markdown("**📊 Feature Statistics:**")
                                                        feature_stats = stage_info['result_data'].get('feature_statistics', {})
                                                        for key, value in feature_stats.items():
                                                            if isinstance(value, float):
                                                                st.text(f"{key.replace('_', ' ').title()}: {value:.2f}")
                                                            else:
                                                                st.text(f"{key.replace('_', ' ').title()}: {value}")
                                                    
                                                    with col2:
                                                        st.markdown("**🎯 Attention Weights:**")
                                                        attention_weights = stage_info['result_data'].get('attention_weights', {})
                                                        for head, weight in attention_weights.items():
                                                            st.text(f"{head.replace('_', ' ').title()}: {weight}")
                                                        
                                                        st.markdown("**🧠 Spatial Encoding:**")
                                                        spatial_data = stage_info['result_data'].get('spatial_encoding', {})
                                                        for key, value in spatial_data.items():
                                                            st.text(f"{key.replace('_', ' ').title()}: {value}")
                                            
                                            elif stage_num == 3:  # Text Detection - Add table
                                                st.markdown("**Input:**")
                                                st.info(stage_info['input'])
                                                st.markdown("**Output:**")
                                                st.success(stage_info['output'])
                                                
                                                # Create character detection table
                                                if 'result_data' in stage_info and 'characters' in stage_info['result_data']:
                                                    st.markdown("**📋 Character Detection Table:**")
                                                    
                                                    import pandas as pd
                                                    
                                                    characters_data = stage_info['result_data']['characters']
                                                    if characters_data:
                                                        # Prepare data for table
                                                        table_data = []
                                                        for char_info in characters_data:
                                                            table_data.append({
                                                                'Text Detected': char_info.get('character', ''),
                                                                'Confidence': f"{char_info.get('confidence', 0):.3f}",
                                                                'Font Size Estimate': char_info.get('font_size_estimate', ''),
                                                                'Is Uppercase': '✅' if char_info.get('is_uppercase', False) else '❌',
                                                                'Stroke Width': char_info.get('stroke_width', ''),
                                                                'Character Quality': char_info.get('character_quality', '')
                                                            })
                                                        
                                                        # Display as table
                                                        df = pd.DataFrame(table_data)
                                                        st.dataframe(df, use_container_width=True)
                                                    
                                                    # Word-level analysis
                                                    if 'words' in stage_info['result_data']:
                                                        st.markdown("**📝 Word Detection Summary:**")
                                                        words_data = stage_info['result_data']['words']
                                                        for i, word_info in enumerate(words_data, 1):
                                                            st.text(f"Word {i}: '{word_info.get('word', '')}' - Confidence: {word_info.get('confidence', 0):.3f}")
                                            
                                            elif stage_num == 4:  # Character Recognition - Unique content
                                                st.markdown("**Input:**")
                                                st.info(stage_info['input'])
                                                st.markdown("**Output:**")
                                                st.success(stage_info['output'])
                                                
                                                if 'result_text' in stage_info:
                                                    st.markdown("**🔤 Recognized Text:**")
                                                    st.code(stage_info['result_text'], language='text')
                                                
                                                # OCR Engine Details
                                                col1, col2 = st.columns(2)
                                                with col1:
                                                    st.markdown("**🤖 OCR Engine Analysis:**")
                                                    details = stage_info.get('details', {})
                                                    st.text(f"Engine: {details.get('ocr_engine', 'N/A')}")
                                                    st.text(f"Character Count: {details.get('character_count', 0)}")
                                                    st.text(f"Word Count: {details.get('word_count', 0)}")
                                                    
                                                with col2:
                                                    st.markdown("**📊 Character Types:**")
                                                    char_types = details.get('character_types', {})
                                                    for char_type, count in char_types.items():
                                                        st.text(f"{char_type.title()}: {count}")
                                            
                                            elif stage_num == 5:  # Post-processing - Unique content
                                                st.markdown("**Input:**")
                                                st.info(stage_info['input'])
                                                st.markdown("**Output:**")
                                                st.success(stage_info['output'])
                                                
                                                if 'result_text' in stage_info:
                                                    st.markdown("**✨ Post-processed Text:**")
                                                    st.code(stage_info['result_text'], language='text')
                                                
                                                # Post-processing details
                                                details = stage_info.get('details', {})
                                                if 'corrections_made' in details:
                                                    st.markdown("**🔧 Corrections Made:**")
                                                    corrections = details['corrections_made']
                                                    if corrections:
                                                        for correction in corrections:
                                                            st.text(f"'{correction.get('original', '')}' → '{correction.get('corrected', '')}' ({correction.get('correction_type', '')})")
                                                    else:
                                                        st.text("No corrections needed - text was already clean!")
                                                
                                                col1, col2 = st.columns(2)
                                                with col1:
                                                    st.markdown("**📈 Processing Stats:**")
                                                    st.text(f"Original Words: {details.get('original_words', 0)}")
                                                    st.text(f"Dictionary Matches: {details.get('dictionary_matches', 0)}")
                                                    st.text(f"Spelling Corrections: {details.get('spelling_corrections', 0)}")
                                                
                                                with col2:
                                                    st.markdown("**🎯 Quality Metrics:**")
                                                    st.text(f"Avg Word Confidence: {details.get('avg_word_confidence', 0):.3f}")
                                                    st.text(f"Final Confidence: {details.get('final_confidence', 0):.3f}")
                                            
                                            elif stage_num == 6:  # Final Output - Unique content
                                                st.markdown("**Input:**")
                                                st.info(stage_info['input'])
                                                st.markdown("**Output:**")
                                                st.success(stage_info['output'])
                                                
                                                if 'result_text' in stage_info:
                                                    st.markdown("**🎉 Final Result:**")
                                                    st.code(stage_info['result_text'], language='text')
                                                
                                                # Final analysis
                                                details = stage_info.get('details', {})
                                                
                                                # Quality assessment
                                                quality = details.get('quality_assessment', {})
                                                st.markdown("**🏆 Quality Assessment:**")
                                                col1, col2, col3 = st.columns(3)
                                                with col1:
                                                    st.metric("Character Accuracy", f"{quality.get('character_accuracy', 0)}%")
                                                with col2:
                                                    st.metric("Word Accuracy", f"{quality.get('word_accuracy', 0)}%")
                                                with col3:
                                                    st.metric("Overall Confidence", f"{details.get('overall_confidence', 0):.3f}")
                                                
                                                # Recommendations
                                                if 'recommendations' in details:
                                                    st.markdown("**💡 Recommendations:**")
                                                    for rec in details['recommendations']:
                                                        st.text(f"• {rec}")
                                            
                                            else:  # Fallback for other stages
                                                col_left, col_right = st.columns([1, 1])
                                                
                                                with col_left:
                                                    st.markdown("**Input:**")
                                                    st.info(stage_info['input'])
                                                    
                                                    if 'result_image' in stage_info and stage_info['result_image']:
                                                        st.markdown("**Processed Image:**")
                                                        st.image(stage_info['result_image'], caption=f"After {stage_info['name']}", width=200)
                                                
                                                with col_right:
                                                    st.markdown("**Output:**")
                                                    st.success(stage_info['output'])
                                                    
                                                    if 'result_text' in stage_info:
                                                        st.markdown("**Extracted Text:**")
                                                        st.code(stage_info['result_text'])
                                                    
                                                    if 'result_data' in stage_info and stage_info['result_data']:
                                                        st.markdown("**Technical Details:**")
                                                        if isinstance(stage_info['result_data'], dict):
                                                            for key, value in stage_info['result_data'].items():
                                                                if not key.startswith('_'):  # Hide private keys
                                                                    st.text(f"{key}: {value}")
                                                        elif isinstance(stage_info['result_data'], list):
                                                            st.text(f"Detected {len(stage_info['result_data'])} items")
                                                            for i, item in enumerate(stage_info['result_data'][:3]):  # Show first 3
                                                                st.text(f"Item {i+1}: {item}")
                                
                                # Show agent processing details
                                with st.expander("📊 Legacy Agent Processing Details"):
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
