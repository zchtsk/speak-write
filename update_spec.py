#!/usr/bin/env python3

import os
import glob

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

def update_spec_file():
    """Update the PyInstaller spec file with the correct snapshot path."""
    snapshot_hash = find_whisper_snapshot()
    
    if not snapshot_hash:
        print("Error: Could not find Whisper model snapshot")
        return False
    
    print(f"Found snapshot: {snapshot_hash}")
    
    spec_file = os.path.join(os.path.dirname(__file__), 'speak-write.spec')
    
    # Read current spec file
    with open(spec_file, 'r') as f:
        content = f.read()
    
    # Generate the new datas section
    base_path = f'models/models--guillaumekln--faster-whisper-tiny/snapshots/{snapshot_hash}'
    new_datas = f"""    datas=[
        ('assets/megaphone.png', 'assets'),
        ('{base_path}/config.json', 'whisper_model/'),
        ('{base_path}/model.bin', 'whisper_model/'),
        ('{base_path}/tokenizer.json', 'whisper_model/'),
        ('{base_path}/vocabulary.txt', 'whisper_model/')
    ],"""
    
    # Replace the datas section
    import re
    pattern = r'datas=\[.*?\],'
    updated_content = re.sub(pattern, new_datas.strip() + ',', content, flags=re.DOTALL)
    
    # Write updated spec file
    with open(spec_file, 'w') as f:
        f.write(updated_content)
    
    print(f"Updated {spec_file} with snapshot {snapshot_hash}")
    return True

if __name__ == "__main__":
    update_spec_file()