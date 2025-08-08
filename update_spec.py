#!/usr/bin/env python3

import os

def find_whisper_snapshot():
    """Find the actual snapshot directory for the whisper model."""
    models_dir = os.path.join(os.path.dirname(__file__), 'models')
    cache_dir = os.path.join(models_dir, 'models--guillaumekln--faster-whisper-tiny')
    
    if not os.path.exists(cache_dir):
        return None
    
    # Read the main ref to get the snapshot hash
    main_ref_file = os.path.join(cache_dir, 'refs', 'main')
    if os.path.exists(main_ref_file):
        with open(main_ref_file, 'r') as f:
            snapshot_hash = f.read().strip()
        
        snapshot_dir = os.path.join(cache_dir, 'snapshots', snapshot_hash)
        if os.path.exists(os.path.join(snapshot_dir, 'model.bin')):
            return snapshot_hash
    
    # Fallback: find any snapshot with model.bin
    snapshots_dir = os.path.join(cache_dir, 'snapshots')
    if os.path.exists(snapshots_dir):
        for snapshot in os.listdir(snapshots_dir):
            snapshot_path = os.path.join(snapshots_dir, snapshot)
            if os.path.exists(os.path.join(snapshot_path, 'model.bin')):
                return snapshot
    
    return None

def generate_spec_file():
    """Generate the PyInstaller spec file from template."""
    snapshot_hash = find_whisper_snapshot()
    
    if not snapshot_hash:
        print("Error: Could not find Whisper model snapshot")
        print("Make sure to run 'python download_model.py' first")
        return False
    
    print(f"Found snapshot: {snapshot_hash}")
    
    template_file = os.path.join(os.path.dirname(__file__), 'speak-write.spec.template')
    spec_file = os.path.join(os.path.dirname(__file__), 'speak-write.spec')
    
    if not os.path.exists(template_file):
        print(f"Error: Template file {template_file} not found")
        return False
    
    # Read template
    with open(template_file, 'r') as f:
        template_content = f.read()
    
    # Generate model paths
    base_path = f'models/models--guillaumekln--faster-whisper-tiny/snapshots/{snapshot_hash}'
    model_paths = f"""('{base_path}/config.json', 'whisper_model/'),
        ('{base_path}/model.bin', 'whisper_model/'),
        ('{base_path}/tokenizer.json', 'whisper_model/'),
        ('{base_path}/vocabulary.txt', 'whisper_model/')"""
    
    # Replace placeholder
    spec_content = template_content.replace('{WHISPER_MODEL_PATHS}', model_paths)
    
    # Write spec file
    with open(spec_file, 'w') as f:
        f.write(spec_content)
    
    print(f"Generated {spec_file} with snapshot {snapshot_hash}")
    return True

if __name__ == "__main__":
    generate_spec_file()