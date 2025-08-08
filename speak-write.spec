# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(
    ['src\\main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('assets/megaphone.png', 'assets'),
        ('models/models--guillaumekln--faster-whisper-tiny/snapshots/ab6d5dcfa0c30295cc49fe2e4ff84a74b4bcffb7/config.json', 'whisper_model/'),
        ('models/models--guillaumekln--faster-whisper-tiny/snapshots/ab6d5dcfa0c30295cc49fe2e4ff84a74b4bcffb7/model.bin', 'whisper_model/'),
        ('models/models--guillaumekln--faster-whisper-tiny/snapshots/ab6d5dcfa0c30295cc49fe2e4ff84a74b4bcffb7/tokenizer.json', 'whisper_model/'),
        ('models/models--guillaumekln--faster-whisper-tiny/snapshots/ab6d5dcfa0c30295cc49fe2e4ff84a74b4bcffb7/vocabulary.txt', 'whisper_model/')
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='speak-write',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['assets\\megaphone.png'],
)
