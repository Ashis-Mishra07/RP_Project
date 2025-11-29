import streamlit as st
from PIL import Image
from vision_agent import vision_agent
import os
from dotenv import load_dotenv
import base64

# Load environment variables
load_dotenv()

# Custom CSS for ultra-modern, attractive UI with animations
def load_custom_css():
    st.markdown("""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&family=Space+Grotesk:wght@400;600;700&display=swap');
    
    /* Global Styles */
    * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Main container with animated gradient */
    .main {
        background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
        padding: 0;
    }
    
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Stunning Header with glassmorphism */
    .main-header {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(30px);
        -webkit-backdrop-filter: blur(30px);
        border: 1px solid rgba(255, 255, 255, 0.3);
        padding: 3rem 2rem;
        border-radius: 30px;
        margin-bottom: 2rem;
        box-shadow: 0 20px 60px rgba(0,0,0,0.3), inset 0 0 0 1px rgba(255,255,255,0.2);
        text-align: center;
        animation: fadeInScale 1s ease-out;
        position: relative;
        overflow: hidden;
    }
    
    .main-header::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
        animation: rotate 20s linear infinite;
    }
    
    @keyframes rotate {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    
    .main-title {
        color: white;
        font-family: 'Space Grotesk', sans-serif;
        font-size: 4.5rem;
        font-weight: 800;
        margin: 0;
        text-shadow: 0 0 20px rgba(255,255,255,0.5), 0 0 40px rgba(255,255,255,0.3), 0 4px 8px rgba(0,0,0,0.3);
        letter-spacing: -2px;
        background: linear-gradient(135deg, #ffffff 0%, #f0f0f0 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        position: relative;
        z-index: 1;
    }
    
    .main-subtitle {
        color: rgba(255,255,255,0.95);
        font-size: 1.5rem;
        font-weight: 600;
        margin: 1rem 0;
        text-shadow: 0 2px 10px rgba(0,0,0,0.3);
        position: relative;
        z-index: 1;
    }
    
    .main-tagline {
        color: rgba(255,255,255,0.85);
        font-size: 1.1rem;
        font-style: italic;
        margin: 0.5rem 0 0 0;
        text-shadow: 0 2px 8px rgba(0,0,0,0.2);
        position: relative;
        z-index: 1;
    }
    
    @keyframes fadeInScale {
        from {
            opacity: 0;
            transform: scale(0.9) translateY(-20px);
        }
        to {
            opacity: 1;
            transform: scale(1) translateY(0);
        }
    }
    
    /* Enhanced glassmorphism cards with hover effects */
    .glass-card {
        background: rgba(255, 255, 255, 0.98);
        border-radius: 25px;
        padding: 2.5rem;
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        box-shadow: 0 15px 50px rgba(0,0,0,0.15), inset 0 0 0 1px rgba(255,255,255,0.4);
        border: 1px solid rgba(255,255,255,0.3);
        margin: 1.5rem 0;
        animation: fadeInUp 0.8s ease-out;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }
    
    .glass-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
        transition: left 0.5s;
    }
    
    .glass-card:hover::before {
        left: 100%;
    }
    
    .glass-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 60px rgba(0,0,0,0.2), inset 0 0 0 1px rgba(255,255,255,0.5);
    }
    
    /* Ultra-modern Sidebar with 3D effect */
    .css-1d391kg, [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 40%, #f093fb 80%, #c471f5 100%) !important;
        background-size: 200% 200%;
        animation: gradientShift 20s ease infinite;
        position: relative;
        border-right: 1px solid rgba(255,255,255,0.1);
        box-shadow: 5px 0 30px rgba(0,0,0,0.2);
    }
    
    /* Animated gradient background */
    @keyframes gradientShift {
        0% { background-position: 0% 0%; }
        50% { background-position: 0% 100%; }
        100% { background-position: 0% 0%; }
    }
    
    /* Multiple overlay effects for depth */
    .css-1d391kg::before, [data-testid="stSidebar"]::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: 
            radial-gradient(circle at 20% 20%, rgba(255,255,255,0.15) 0%, transparent 50%),
            radial-gradient(circle at 80% 80%, rgba(255,255,255,0.1) 0%, transparent 50%);
        pointer-events: none;
        z-index: 1;
    }
    
    .css-1d391kg::after, [data-testid="stSidebar"]::after {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(180deg, rgba(255,255,255,0.05) 0%, transparent 50%, rgba(0,0,0,0.05) 100%);
        pointer-events: none;
        z-index: 1;
    }
    
    /* Sidebar headers with enhanced glow and 3D effect */
    .css-1d391kg h1, .css-1d391kg h2, .css-1d391kg h3,
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {
        color: white !important;
        text-shadow: 
            0 0 30px rgba(255,255,255,0.6), 
            0 0 60px rgba(255,255,255,0.4),
            0 4px 10px rgba(0,0,0,0.3);
        font-weight: 800 !important;
        letter-spacing: 0.5px;
        position: relative;
        z-index: 2;
        font-family: 'Space Grotesk', sans-serif !important;
    }
    
    /* Sidebar text with better readability */
    .css-1d391kg p, [data-testid="stSidebar"] p,
    .css-1d391kg span, [data-testid="stSidebar"] span,
    .css-1d391kg label, [data-testid="stSidebar"] label {
        color: rgba(255,255,255,0.98) !important;
        font-weight: 500;
        text-shadow: 0 2px 8px rgba(0,0,0,0.2);
        position: relative;
        z-index: 2;
    }
    
    /* Enhanced sidebar divider with glow */
    .css-1d391kg hr, [data-testid="stSidebar"] hr {
        border: none !important;
        height: 2px;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.5), transparent);
        margin: 2rem 0;
        box-shadow: 0 0 10px rgba(255,255,255,0.3);
        position: relative;
        z-index: 2;
    }
    
    /* Modern 3D Button with micro-interactions */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 50px;
        padding: 1rem 2.5rem;
        font-weight: 700;
        font-size: 1.15rem;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4), inset 0 -4px 0 rgba(0,0,0,0.1);
        position: relative;
        overflow: hidden;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .stButton > button::before {
        content: '';
        position: absolute;
        top: 50%;
        left: 50%;
        width: 0;
        height: 0;
        border-radius: 50%;
        background: rgba(255,255,255,0.3);
        transform: translate(-50%, -50%);
        transition: width 0.6s, height 0.6s;
    }
    
    .stButton > button:hover::before {
        width: 300px;
        height: 300px;
    }
    
    .stButton > button:hover {
        transform: translateY(-4px) scale(1.02);
        box-shadow: 0 12px 35px rgba(102, 126, 234, 0.6), inset 0 -4px 0 rgba(0,0,0,0.15);
    }
    
    .stButton > button:active {
        transform: translateY(-1px) scale(0.98);
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4), inset 0 2px 0 rgba(0,0,0,0.2);
    }
    
    /* Enhanced file uploader with pulse animation */
    .uploadedFile {
        border-radius: 20px;
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
        border: 3px dashed #667eea;
        padding: 3rem;
        text-align: center;
        transition: all 0.4s ease;
        position: relative;
        overflow: hidden;
    }
    
    .uploadedFile::before {
        content: '';
        position: absolute;
        top: 50%;
        left: 50%;
        width: 100px;
        height: 100px;
        border: 2px solid rgba(102, 126, 234, 0.3);
        border-radius: 50%;
        transform: translate(-50%, -50%);
        animation: pulse 2s ease-in-out infinite;
    }
    
    @keyframes pulse {
        0%, 100% {
            transform: translate(-50%, -50%) scale(0.8);
            opacity: 1;
        }
        50% {
            transform: translate(-50%, -50%) scale(1.5);
            opacity: 0;
        }
    }
    
    .uploadedFile:hover {
        border-color: #764ba2;
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.15) 0%, rgba(118, 75, 162, 0.15) 100%);
        transform: scale(1.02);
    }
    
    /* Animated progress bar with glow */
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        background-size: 200% 100%;
        animation: progressShine 2s ease infinite;
        box-shadow: 0 0 20px rgba(102, 126, 234, 0.6);
        border-radius: 10px;
    }
    
    @keyframes progressShine {
        0% { background-position: 0% 0%; }
        50% { background-position: 100% 0%; }
        100% { background-position: 0% 0%; }
    }
    
    /* Enhanced metrics with 3D effect */
    [data-testid="stMetricValue"] {
        font-size: 2.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 4px 10px rgba(102, 126, 234, 0.3);
        font-family: 'Space Grotesk', sans-serif;
    }
    
    /* Modern expander with hover effect */
    .streamlit-expanderHeader {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
        border-radius: 15px;
        font-weight: 700;
        padding: 1rem 1.5rem;
        transition: all 0.3s ease;
        border: 1px solid rgba(102, 126, 234, 0.2);
    }
    
    .streamlit-expanderHeader:hover {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.2) 0%, rgba(118, 75, 162, 0.2) 100%);
        transform: translateX(5px);
        box-shadow: -5px 0 15px rgba(102, 126, 234, 0.2);
    }
    
    /* Stunning result box with 3D depth */
    .result-box {
        background: linear-gradient(135deg, rgba(255,255,255,0.95) 0%, rgba(255,255,255,0.9) 100%);
        border-left: 8px solid;
        border-image: linear-gradient(180deg, #667eea 0%, #764ba2 100%) 1;
        border-radius: 20px;
        padding: 2.5rem;
        margin: 2rem 0;
        box-shadow: 0 15px 40px rgba(0,0,0,0.15), inset 0 0 0 1px rgba(102,126,234,0.1);
        animation: slideInLeft 0.6s ease-out;
        position: relative;
        overflow: hidden;
        transition: all 0.4s ease;
    }
    
    .result-box::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 5px;
        height: 100%;
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
        box-shadow: 0 0 20px rgba(102, 126, 234, 0.6);
    }
    
    .result-box:hover {
        transform: translateX(5px);
        box-shadow: 0 20px 50px rgba(0,0,0,0.2), inset 0 0 0 1px rgba(102,126,234,0.2);
    }
    
    .result-title {
        color: #667eea;
        font-size: 1.8rem;
        font-weight: 700;
        margin-bottom: 1.5rem;
        font-family: 'Space Grotesk', sans-serif;
        text-shadow: 0 2px 10px rgba(102, 126, 234, 0.2);
    }
    
    .result-text {
        color: #1a202c;
        font-size: 2.5rem;
        font-weight: 800;
        line-height: 1.5;
        text-align: center;
        padding: 2rem;
        background: linear-gradient(135deg, #ffffff 0%, #f7fafc 100%);
        border-radius: 15px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.08), inset 0 2px 0 rgba(255,255,255,0.5);
        letter-spacing: 0.5px;
        font-family: 'Space Grotesk', sans-serif;
    }
    
    /* Dynamic stage indicator with badge design */
    .stage-indicator {
        display: inline-block;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.6rem 1.5rem;
        border-radius: 50px;
        font-weight: 700;
        font-size: 0.95rem;
        margin: 0.5rem;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4), inset 0 -2px 0 rgba(0,0,0,0.1);
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 1px;
        position: relative;
        overflow: hidden;
    }
    
    .stage-indicator::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
        transition: left 0.5s;
    }
    
    .stage-indicator:hover {
        transform: translateY(-2px) scale(1.05);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.5), inset 0 -2px 0 rgba(0,0,0,0.15);
    }
    
    .stage-indicator:hover::before {
        left: 100%;
    }
    
    /* Enhanced animations library */
    @keyframes fadeInDown {
        from {
            opacity: 0;
            transform: translateY(-40px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(40px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes slideInLeft {
        from {
            opacity: 0;
            transform: translateX(-50px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    @keyframes slideInRight {
        from {
            opacity: 0;
            transform: translateX(50px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    @keyframes bounceIn {
        0% {
            opacity: 0;
            transform: scale(0.3);
        }
        50% {
            transform: scale(1.05);
        }
        70% {
            transform: scale(0.9);
        }
        100% {
            opacity: 1;
            transform: scale(1);
        }
    }
    
    @keyframes float {
        0%, 100% {
            transform: translateY(0px);
        }
        50% {
            transform: translateY(-10px);
        }
    }
    
    /* Advanced info boxes with icons */
    .info-box {
        background: linear-gradient(135deg, rgba(52, 211, 153, 0.1) 0%, rgba(16, 185, 129, 0.1) 100%);
        border-left: 5px solid #10b981;
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        animation: slideInRight 0.6s ease-out;
        box-shadow: 0 4px 15px rgba(16, 185, 129, 0.1);
        transition: all 0.3s ease;
    }
    
    .info-box:hover {
        transform: translateX(5px);
        box-shadow: 0 6px 20px rgba(16, 185, 129, 0.2);
    }
    
    .warning-box {
        background: linear-gradient(135deg, rgba(251, 191, 36, 0.1) 0%, rgba(245, 158, 11, 0.1) 100%);
        border-left: 5px solid #f59e0b;
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        animation: bounceIn 0.8s ease-out;
        box-shadow: 0 4px 15px rgba(245, 158, 11, 0.1);
    }
    
    .error-box {
        background: linear-gradient(135deg, rgba(239, 68, 68, 0.1) 0%, rgba(220, 38, 38, 0.1) 100%);
        border-left: 5px solid #ef4444;
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        animation: bounceIn 0.8s ease-out;
        box-shadow: 0 4px 15px rgba(239, 68, 68, 0.1);
    }
    
    /* Floating particles effect (optional decoration) */
    .particles {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: -1;
    }
    
    /* Success animation */
    @keyframes successPulse {
        0% {
            box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7);
        }
        70% {
            box-shadow: 0 0 0 20px rgba(16, 185, 129, 0);
        }
        100% {
            box-shadow: 0 0 0 0 rgba(16, 185, 129, 0);
        }
    }
    
    /* Loading spinner */
    @keyframes spin {
        from {
            transform: rotate(0deg);
        }
        to {
            transform: rotate(360deg);
        }
    }
    
    /* Image container with hover zoom */
    .image-container {
        position: relative;
        overflow: hidden;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        transition: all 0.4s ease;
    }
    
    .image-container:hover {
        transform: scale(1.02);
        box-shadow: 0 15px 40px rgba(0,0,0,0.3);
    }
    
    .image-container img {
        transition: transform 0.4s ease;
    }
    
    .image-container:hover img {
        transform: scale(1.1);
    }
    
    /* Tooltip styling */
    .tooltip {
        position: relative;
        display: inline-block;
    }
    
    .tooltip .tooltiptext {
        visibility: hidden;
        background-color: rgba(0, 0, 0, 0.9);
        color: white;
        text-align: center;
        border-radius: 10px;
        padding: 0.5rem 1rem;
        position: absolute;
        z-index: 1;
        bottom: 125%;
        left: 50%;
        transform: translateX(-50%);
        opacity: 0;
        transition: opacity 0.3s, visibility 0.3s;
    }
    
    .tooltip:hover .tooltiptext {
        visibility: visible;
        opacity: 1;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Responsive design */
    @media (max-width: 768px) {
        .main-title {
            font-size: 3rem;
        }
        
        .result-text {
            font-size: 1.8rem;
        }
        
        .glass-card {
            padding: 1.5rem;
        }
        
        .success-alert {
            background: linear-gradient(135deg, #48bb7815 0%, #48bb7825 100%);
            border-radius: 10px;
            padding: 1rem;
            color: #2f855a;
            font-weight: 600;
        }
        
        /* Hide Streamlit branding */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        
        /* Custom scrollbar */
        ::-webkit-scrollbar {
            width: 10px;
        }
        
        ::-webkit-scrollbar-track {
            background: #f1f1f1;
            border-radius: 10px;
        }
        
        ::-webkit-scrollbar-thumb {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 10px;
        }
        
        ::-webkit-scrollbar-thumb:hover {
            background: #764ba2;
        }
    }
    </style>
    """, unsafe_allow_html=True)


def main():
    """
    Advanced Vision-Language Agent for Text Recognition
    """
    # Page configuration
    st.set_page_config(
        page_title="VisionText Agent v3.2.1",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Load custom CSS
    load_custom_css()
    
    # Modern header with gradient
    st.markdown("""
    <div class="main-header">
        <h1 class="main-title">🤖 VisionText Agent</h1>
        <p class="main-subtitle">Advanced Multi-Stage Text Recognition System</p>
        <p class="main-tagline">Powered by Vision Transformer and Multi-Modal AI Architecture</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Modern Sidebar with enhanced glassmorphism effects
    with st.sidebar:
        # Animated header with emoji
        st.markdown("""
        <div style="
            text-align: center;
            padding: 1.5rem 0;
            margin-bottom: 1rem;
            background: rgba(255,255,255,0.1);
            border-radius: 20px;
            backdrop-filter: blur(10px);
            box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        ">
            <div style="font-size: 3rem; margin-bottom: 0.5rem;">🤖</div>
            <div style="font-size: 1.5rem; font-weight: 700; color: white; text-shadow: 0 2px 10px rgba(0,0,0,0.3);">
                Agent System
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Get agent info
        agent_info = vision_agent.get_agent_info()
        
        # Test agent system with modern loading animation
        with st.spinner("🔄 Initializing Agent System..."):
            is_ready, status_msg = vision_agent.test_agent_system()
            
        if is_ready:
            st.markdown("""
            <div style="
                background: linear-gradient(135deg, rgba(72,187,120,0.2) 0%, rgba(72,187,120,0.3) 100%);
                border-left: 4px solid #48bb78;
                border-radius: 12px;
                padding: 1rem;
                color: white;
                font-weight: 600;
                margin: 1rem 0;
                box-shadow: 0 4px 15px rgba(72,187,120,0.2);
            ">
                ✅ Agent System Operational!
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div style="
                background: rgba(255,255,255,0.15);
                border-radius: 15px;
                padding: 1rem;
                margin: 1rem 0;
                text-align: center;
                backdrop-filter: blur(5px);
                border: 1px solid rgba(255,255,255,0.2);
            ">
                <div style="font-size: 1.2rem; font-weight: 700; color: white; margin-bottom: 0.3rem;">
                    🤖 {agent_info['agent_name']}
                </div>
                <div style="
                    display: inline-block;
                    background: rgba(255,255,255,0.25);
                    padding: 0.3rem 0.8rem;
                    border-radius: 20px;
                    font-size: 0.9rem;
                    font-weight: 600;
                    color: white;
                ">
                    v{agent_info['version']}
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.error(f"❌ {status_msg}")
        
        st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)
        
        # Show agent components with enhanced cards
        st.markdown("""
        <div style="
            background: rgba(255,255,255,0.1);
            border-radius: 15px;
            padding: 1rem;
            margin: 1rem 0;
            backdrop-filter: blur(5px);
        ">
            <div style="
                font-size: 1.3rem;
                font-weight: 700;
                color: white;
                margin-bottom: 1rem;
                text-align: center;
            ">
                🧠 Agent Components
            </div>
        """, unsafe_allow_html=True)
        
        for i, stage in enumerate(agent_info['processing_pipeline'], 1):
            # Animated component cards with hover effect
            st.markdown(f"""
            <div style="
                background: rgba(255,255,255,0.15);
                padding: 1rem;
                border-radius: 12px;
                margin: 0.6rem 0;
                border-left: 4px solid white;
                backdrop-filter: blur(10px);
                transition: all 0.3s ease;
                cursor: pointer;
                box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            " onmouseover="this.style.transform='translateX(5px)'; this.style.background='rgba(255,255,255,0.25)';"
               onmouseout="this.style.transform='translateX(0)'; this.style.background='rgba(255,255,255,0.15)';">
                <div style="
                    display: flex;
                    align-items: center;
                    color: white;
                    font-weight: 600;
                ">
                    <span style="
                        background: rgba(255,255,255,0.3);
                        border-radius: 50%;
                        width: 28px;
                        height: 28px;
                        display: inline-flex;
                        align-items: center;
                        justify-content: center;
                        margin-right: 0.8rem;
                        font-size: 0.9rem;
                    ">{i}</span>
                    <span>{stage}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)
        
        # Performance metrics with modern animated cards
        st.markdown("""
        <div style="
            background: rgba(255,255,255,0.1);
            border-radius: 15px;
            padding: 1rem;
            margin: 1rem 0;
            backdrop-filter: blur(5px);
        ">
            <div style="
                font-size: 1.3rem;
                font-weight: 700;
                color: white;
                margin-bottom: 1rem;
                text-align: center;
            ">
                📊 Performance
            </div>
        """, unsafe_allow_html=True)
        
        perf = agent_info['performance']
        
        # Accuracy metric with circular progress feel
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, rgba(255,255,255,0.2) 0%, rgba(255,255,255,0.1) 100%);
            padding: 1.5rem;
            border-radius: 15px;
            margin: 0.8rem 0;
            text-align: center;
            backdrop-filter: blur(10px);
            border: 2px solid rgba(255,255,255,0.2);
            box-shadow: 0 8px 25px rgba(0,0,0,0.15);
            animation: scaleIn 0.5s ease-out;
        ">
            <div style="
                font-size: 3rem;
                margin-bottom: 0.5rem;
                animation: bounce 2s ease-in-out infinite;
            ">🎯</div>
            <div style="
                font-size: 2.5rem;
                font-weight: 900;
                color: white;
                text-shadow: 0 2px 10px rgba(0,0,0,0.3);
                margin-bottom: 0.3rem;
            ">{perf['accuracy']}</div>
            <div style="
                font-size: 1rem;
                color: rgba(255,255,255,0.85);
                font-weight: 600;
                letter-spacing: 1px;
            ">Accuracy</div>
        </div>
        
        <div style="
            background: linear-gradient(135deg, rgba(255,255,255,0.2) 0%, rgba(255,255,255,0.1) 100%);
            padding: 1.5rem;
            border-radius: 15px;
            margin: 0.8rem 0;
            text-align: center;
            backdrop-filter: blur(10px);
            border: 2px solid rgba(255,255,255,0.2);
            box-shadow: 0 8px 25px rgba(0,0,0,0.15);
            animation: scaleIn 0.6s ease-out;
        ">
            <div style="
                font-size: 3rem;
                margin-bottom: 0.5rem;
                animation: bounce 2s ease-in-out infinite 0.2s;
            ">⚡</div>
            <div style="
                font-size: 2rem;
                font-weight: 900;
                color: white;
                text-shadow: 0 2px 10px rgba(0,0,0,0.3);
                margin-bottom: 0.3rem;
            ">{perf['speed']}</div>
            <div style="
                font-size: 1rem;
                color: rgba(255,255,255,0.85);
                font-weight: 600;
                letter-spacing: 1px;
            ">Processing Speed</div>
        </div>
        
        <div style="
            background: linear-gradient(135deg, rgba(255,255,255,0.2) 0%, rgba(255,255,255,0.1) 100%);
            padding: 1.5rem;
            border-radius: 15px;
            margin: 0.8rem 0;
            text-align: center;
            backdrop-filter: blur(10px);
            border: 2px solid rgba(255,255,255,0.2);
            box-shadow: 0 8px 25px rgba(0,0,0,0.15);
            animation: scaleIn 0.7s ease-out;
        ">
            <div style="
                font-size: 3rem;
                margin-bottom: 0.5rem;
                animation: bounce 2s ease-in-out infinite 0.4s;
            ">🌍</div>
            <div style="
                font-size: 2rem;
                font-weight: 900;
                color: white;
                text-shadow: 0 2px 10px rgba(0,0,0,0.3);
                margin-bottom: 0.3rem;
            ">{perf['languages']}</div>
            <div style="
                font-size: 1rem;
                color: rgba(255,255,255,0.85);
                font-weight: 600;
                letter-spacing: 1px;
            ">Languages Supported</div>
        </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Add custom animations
        st.markdown("""
        <style>
        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.02); }
        }
        
        @keyframes slideInRight {
            from {
                opacity: 0;
                transform: translateX(-20px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }
        
        @keyframes scaleIn {
            from {
                opacity: 0;
                transform: scale(0.9);
            }
            to {
                opacity: 1;
                transform: scale(1);
            }
        }
        
        @keyframes bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }
        </style>
        """, unsafe_allow_html=True)
    
    # Single unified upload section
    # st.markdown("""
    # <div class="glass-card" style="text-align: center;">
    #     <div style="
    #         background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    #         -webkit-background-clip: text;
    #         -webkit-text-fill-color: transparent;
    #         background-clip: text;
    #         margin-bottom: 1rem;
    #     ">
    #         <h1 style="font-size: 3rem; margin: 0;">📤</h1>
    #         <h2 style="font-size: 2rem; font-weight: 700; margin: 0.5rem 0;">Upload Your Image</h2>
    #     </div>
    #     <p style="color: #718096; font-size: 1.1rem; margin-bottom: 2rem;">
    #         🎯 Choose an image containing text for AI-powered recognition<br>
    #         <span style="font-size: 0.9rem; color: #a0aec0;">Supports: PNG, JPG, JPEG, BMP, TIFF • Max: 200MB</span>
    #     </p>
    # </div>
    # """, unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader(
        "Drop your image here or click to browse",
        type=['png', 'jpg', 'jpeg', 'bmp', 'tiff', 'tif'],
        help="Supported formats: PNG, JPG, JPEG, BMP, TIFF",
        label_visibility="collapsed"
    )
    
    if uploaded_file is not None:
        # Display uploaded image with modern styling
        image = Image.open(uploaded_file)
        
        st.markdown("""
        <div class="glass-card">
            <h2 style="color: #667eea;">📷 Image Preview</h2>
        </div>
        """, unsafe_allow_html=True)
        
        # Create modern layout
        col1, col2 = st.columns([1, 1], gap="large")
        
        with col1:
            # Image display with shadow effect
            st.image(
                image, 
                caption="📸 Uploaded Image",
                use_container_width=True
            )
            
            # Image info in modern card
            st.markdown(f"""
            <div class="info-box">
                <h4 style="color: #667eea; margin: 0 0 0.5rem 0;">📊 Image Details</h4>
                <div style="display: flex; justify-content: space-between; margin: 0.3rem 0;">
                    <span>📐 Dimensions:</span>
                    <span style="font-weight: 600;">{image.size[0]} × {image.size[1]} px</span>
                </div>
                <div style="display: flex; justify-content: space-between; margin: 0.3rem 0;">
                    <span>📁 Format:</span>
                    <span style="font-weight: 600;">{image.format}</span>
                </div>
                <div style="display: flex; justify-content: space-between; margin: 0.3rem 0;">
                    <span>🎨 Mode:</span>
                    <span style="font-weight: 600;">{image.mode}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div style="
                background: linear-gradient(135deg, #667eea15 0%, #764ba215 100%);
                padding: 2rem;
                border-radius: 15px;
                height: 100%;
                display: flex;
                flex-direction: column;
                justify-content: center;
            ">
                <h3 style="color: #667eea; margin-bottom: 1rem;">🚀 Ready to Process</h3>
                <p style="color: #4a5568; margin-bottom: 1.5rem;">
                    Click the button below to start the AI-powered text recognition process.
                    The agent will analyze your image through 6 advanced processing stages.
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            # Check if agent is ready
            if vision_agent.is_ready:
                # Modern process button
                if st.button("🚀 Start AI Processing", type="primary", use_container_width=True):
                    
                    # Processing section with modern design
                    st.markdown("""
                    <div class="glass-card" style="margin-top: 2rem;">
                        <h2 style="color: #667eea;">⚙️ AI Processing</h2>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Progress tracking with modern design
                    progress_container = st.container()
                    
                    with progress_container:
                        # Modern progress bar
                        progress_bar = st.progress(0)
                        status_text = st.empty()
                        
                        # Stage visualization
                        stages_container = st.empty()
                        
                        def update_progress(stage_msg, progress):
                            progress_bar.progress(progress / 100)
                            status_text.markdown(f"""
                            <div style="
                                text-align: center;
                                padding: 1rem;
                                background: linear-gradient(135deg, #667eea10 0%, #764ba210 100%);
                                border-radius: 10px;
                                margin: 1rem 0;
                            ">
                                <span style="font-size: 1.2rem; color: #667eea; font-weight: 600;">
                                    🤖 {stage_msg}
                                </span>
                            </div>
                            """, unsafe_allow_html=True)
                        
                        # Process with agent
                        predicted_text, stage_results = vision_agent.process_image_with_agent(
                            image, 
                            progress_callback=update_progress
                        )
                        
                        # Completion animation
                        progress_bar.progress(100)
                        status_text.markdown("""
                        <div style="
                            text-align: center;
                            padding: 1.5rem;
                            background: linear-gradient(135deg, #48bb7815 0%, #48bb7825 100%);
                            border-radius: 15px;
                            margin: 1rem 0;
                        ">
                            <span style="font-size: 1.5rem; color: #38a169; font-weight: 700;">
                                ✅ Processing Complete!
                            </span>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    # Results section with modern design
                    if predicted_text and predicted_text != "No text detected" and not predicted_text.startswith("Error"):
                        
                        # Success message
                        st.markdown("""
                        <div class="glass-card">
                            <h2 style="color: #38a169;">✅ Recognition Successful!</h2>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        # Display result in beautiful card
                        st.markdown(f"""
                        <div class="result-box">
                            <div class="result-title">🤖 AI Detected Text:</div>
                            <div class="result-text">{predicted_text}</div>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        # Detailed analysis section
                        st.markdown("""
                        <div class="glass-card">
                            <h2 style="color: #667eea;">🔬 Detailed Stage Analysis</h2>
                            <p style="color: #718096;">Explore each processing stage in detail</p>
                        </div>
                        """, unsafe_allow_html=True)
                        
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
                        # Error or no detection
                        if predicted_text.startswith("Error"):
                            st.markdown(f"""
                            <div style="
                                background: linear-gradient(135deg, #fc8b8115 0%, #fc8b8125 100%);
                                border-left: 5px solid #fc8181;
                                border-radius: 15px;
                                padding: 2rem;
                                margin: 1.5rem 0;
                            ">
                                <h3 style="color: #c53030;">❌ Processing Error</h3>
                                <p style="color: #742a2a; font-size: 1.1rem;">{predicted_text}</p>
                            </div>
                            """, unsafe_allow_html=True)
                        else:
                            st.markdown("""
                            <div style="
                                background: linear-gradient(135deg, #ecc94b15 0%, #ecc94b25 100%);
                                border-left: 5px solid #ecc94b;
                                border-radius: 15px;
                                padding: 2rem;
                                margin: 1.5rem 0;
                            ">
                                <h3 style="color: #b7791f;">⚠️ No Text Detected</h3>
                                <p style="color: #744210; font-size: 1.1rem;">
                                    The AI couldn't detect any text in this image.
                                </p>
                                
                                <h4 style="color: #b7791f; margin-top: 1.5rem;">💡 Optimization Tips:</h4>
                                <ul style="color: #744210;">
                                    <li>Ensure the text is clear and readable</li>
                                    <li>Use images with good contrast</li>
                                    <li>Avoid blurry or low-resolution images</li>
                                    <li>Make sure the text is not too small</li>
                                </ul>
                            </div>
                            """, unsafe_allow_html=True)
            else:
                st.error("❌ Agent system not ready. Please check configuration!")
    
    else:
        # Welcome screen with modern design
        st.markdown("""
        <div class="glass-card" style="text-align: center; padding: 3rem;">
            <div style="font-size: 5rem; margin-bottom: 1rem;">📸</div>
            <h2 style="color: #667eea; margin-bottom: 1rem;">Ready to Recognize Text</h2>
            <p style="color: #718096; font-size: 1.2rem; margin-bottom: 2rem;">
                Upload an image to experience AI-powered text recognition
            </p>
            <p style="color: #a0aec0;">
                Supports: PNG, JPG, JPEG, BMP, TIFF formats
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Architecture overview
        # st.markdown("""
        # <div class="glass-card">
        #     <h2 style="color: #667eea; margin-bottom: 1.5rem;">🤖 Agent Architecture</h2>
        # </div>
        # """, unsafe_allow_html=True)
        
        agent_info = vision_agent.get_agent_info()
        
        # Pipeline and models in columns
        col1, col2 = st.columns(2, gap="large")
        
        with col1:
            st.markdown("""
            <div class="info-box">
                <h3 style="color: #667eea;">🧠 Processing Pipeline</h3>
            </div>
            """, unsafe_allow_html=True)
            
            for i, stage in enumerate(agent_info['processing_pipeline'], 1):
                st.markdown(f"""
                <div style="
                    background: linear-gradient(135deg, #667eea10 0%, #764ba210 100%);
                    padding: 1rem;
                    border-radius: 10px;
                    margin: 0.5rem 0;
                    border-left: 4px solid #667eea;
                ">
                    <b>Stage {i}:</b> {stage}
                </div>
                """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="info-box">
                <h3 style="color: #667eea;">🔧 AI Models</h3>
            </div>
            """, unsafe_allow_html=True)
            
            for model in agent_info['models_used']:
                st.markdown(f"""
                <div style="
                    background: linear-gradient(135deg, #764ba210 0%, #667eea10 100%);
                    padding: 1rem;
                    border-radius: 10px;
                    margin: 0.5rem 0;
                    border-left: 4px solid #764ba2;
                ">
                    • {model}
                </div>
                """, unsafe_allow_html=True)
        
        # Performance metrics
        st.markdown("""
        <div class="glass-card">
            <h2 style="color: #667eea; margin-bottom: 1.5rem;">📊 Performance Metrics</h2>
        </div>
        """, unsafe_allow_html=True)
        
        perf_col1, perf_col2, perf_col3 = st.columns(3)
        
        perf = agent_info['performance']
        
        with perf_col1:
            st.markdown(f"""
            <div style="
                background: linear-gradient(135deg, #667eea15 0%, #764ba215 100%);
                padding: 2rem;
                border-radius: 15px;
                text-align: center;
                box-shadow: 0 4px 15px rgba(102, 126, 234, 0.2);
            ">
                <div style="font-size: 3rem; margin-bottom: 0.5rem;">🎯</div>
                <div style="font-size: 2rem; font-weight: 700; color: #667eea;">{perf['accuracy']}</div>
                <div style="color: #718096; margin-top: 0.5rem;">Accuracy</div>
            </div>
            """, unsafe_allow_html=True)
        
        with perf_col2:
            st.markdown(f"""
            <div style="
                background: linear-gradient(135deg, #667eea15 0%, #764ba215 100%);
                padding: 2rem;
                border-radius: 15px;
                text-align: center;
                box-shadow: 0 4px 15px rgba(102, 126, 234, 0.2);
            ">
                <div style="font-size: 3rem; margin-bottom: 0.5rem;">⚡</div>
                <div style="font-size: 2rem; font-weight: 700; color: #667eea;">{perf['speed']}</div>
                <div style="color: #718096; margin-top: 0.5rem;">Speed</div>
            </div>
            """, unsafe_allow_html=True)
        
        with perf_col3:
            st.markdown(f"""
            <div style="
                background: linear-gradient(135deg, #667eea15 0%, #764ba215 100%);
                padding: 2rem;
                border-radius: 15px;
                text-align: center;
                box-shadow: 0 4px 15px rgba(102, 126, 234, 0.2);
            ">
                <div style="font-size: 3rem; margin-bottom: 0.5rem;">🌍</div>
                <div style="font-size: 2rem; font-weight: 700; color: #667eea;">{perf['languages']}</div>
                <div style="color: #718096; margin-top: 0.5rem;">Languages</div>
            </div>
            """, unsafe_allow_html=True)
    
    # Modern footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 2rem; color: #a0aec0;">
        <p style="font-size: 1.1rem; font-weight: 600; color: #667eea; margin-bottom: 0.5rem;">
            VisionText Agent v3.2.1
        </p>
        <p style="font-size: 0.9rem;">
            Powered by Advanced Vision-Language Architecture | © 2025
        </p>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
