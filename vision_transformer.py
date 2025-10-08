import torch
import torch.nn as nn
from transformers import ViTImageProcessor, ViTForImageClassification
from PIL import Image
import numpy as np

class VisionTransformerFeatureExtractor:
    def __init__(self):
        """Initialize Vision Transformer for feature extraction"""
        self.processor = ViTImageProcessor.from_pretrained('google/vit-base-patch16-224')
        self.model = ViTForImageClassification.from_pretrained('google/vit-base-patch16-224')
        self.model.eval()
    
    def extract_features(self, image):
        """
        Extract features from image using Vision Transformer
        
        Args:
            image: PIL Image object
            
        Returns:
            numpy.ndarray: Feature vector from ViT
        """
        try:
            # Preprocess image
            inputs = self.processor(images=image, return_tensors="pt")
            
            # Extract features (before classification layer)
            with torch.no_grad():
                outputs = self.model(**inputs, output_hidden_states=True)
                # Get last hidden state (features)
                features = outputs.hidden_states[-1]
                # Global average pooling
                features = features.mean(dim=1).squeeze().numpy()
            
            return features
            
        except Exception as e:
            print(f"Feature extraction error: {e}")
            return None
    
    def analyze_spatial_relationships(self, image):
        """
        Analyze spatial relationships in the image
        """
        try:
            inputs = self.processor(images=image, return_tensors="pt")
            
            with torch.no_grad():
                outputs = self.model(**inputs, output_attentions=True)
                # Get attention weights for spatial analysis
                attention_weights = outputs.attentions[-1]
                
            return attention_weights.numpy()
            
        except Exception as e:
            print(f"Spatial analysis error: {e}")
            return None

# Usage in your pipeline
def integrate_vision_transformer(image):
    """
    Integrate Vision Transformer into your existing pipeline
    """
    vit_extractor = VisionTransformerFeatureExtractor()
    
    # Extract features
    features = vit_extractor.extract_features(image)
    
    # Analyze spatial relationships
    attention_maps = vit_extractor.analyze_spatial_relationships(image)
    
    return features, attention_maps