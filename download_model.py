#!/usr/bin/env python3

import os
from faster_whisper import WhisperModel

def download_whisper_model():
    """Download and cache the Whisper tiny model locally."""
    
    # Create models directory
    models_dir = os.path.join(os.path.dirname(__file__), 'models')
    os.makedirs(models_dir, exist_ok=True)
    
    print("Downloading Whisper tiny model...")
    
    # Initialize model - this will download it to the default cache location
    # We'll then copy it to our local models directory
    model = WhisperModel("tiny", device="cpu", compute_type="int8", download_root=models_dir)
    
    print(f"Model downloaded to: {models_dir}")
    print("Model is ready for inclusion in executable.")
    
    return models_dir

if __name__ == "__main__":
    download_whisper_model()