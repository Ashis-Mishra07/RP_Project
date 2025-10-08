Code Flow:
app.py → preprocess.py → Enhanced Image → Stage 2
Enhanced Image → ai_vision.py → Gemini Vision API → Features → Stage 3
Features → vision_agent/ → Text Regions → Stage 4
Text Regions → predict.py → Multiple OCR Engines → Raw Text → Stage 5
Raw Text → vision_agent/ → Corrected Text → Stage 6
Corrected Text → test_system/ → Confidence Scores → Final Output


Vision Transformer

The Vision Transformer is a deep learning model designed for image recognition tasks, inspired by the Transformer architecture that originally revolutionized Natural Language Processing (NLP) (like GPT and BERT).

Image → Split into patches → Linear Embedding + Positional Encoding
      → Transformer Encoder Blocks
      → Classification Token Output → Softmax → Label



User Interaction Flow:
1. User uploads image via app.py (Streamlit interface)
2. Image validation and format conversion
3. Preprocessing pipeline activation (preprocess.py)
4. Multi-stage agent processing (vision_agent/)
5. AI-powered recognition (ai_vision.py + gemini_vision/)
6. Alternative OCR processing (google_vision/)
7. Prediction orchestration (predict.py)
8. Results aggregation and confidence scoring
9. Final output display with metrics


Technical Data Flow:

Image Upload → app.py
     ↓
Format Validation → preprocess.py
     ↓
Stage 1: CLAHE + Otsu → preprocess.py
     ↓
Stage 2: Vision Transformer → vision_transformer.py
     ↓
Stage 3: Text Detection → vision_agent/
     ↓
Stage 4: Multi-OCR Recognition → predict.py
     ↓
Stage 5: Dictionary + N-gram → vision_agent/
     ↓
Stage 6: Confidence Scoring → test_system/
     ↓
Final Results → app.py (Display)







