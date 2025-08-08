# Speak-Write

Speak-Write is a fast, lightweight, and privacy-focused voice-to-text desktop application that transforms your spoken words into text anywhere on your computer. Built with OpenAI's Whisper model, it provides accurate speech recognition while keeping all your data completely private.

## Why Speak-Write?

In an era where most voice recognition services send your audio to remote servers, Speak-Write takes a different approach. Everything happens locally on your machine - no internet connection required, no data transmitted, and no privacy concerns.

## Key Features

- **Completely Private**: All audio processing happens locally on your device
- **Universal Input**: Works in any application - text editors, browsers, chat apps, documents
- **Instant Transcription**: Fast speech-to-text using optimized Whisper model
- **Simple Hotkey**: Just press Ctrl+Shift+0 to record and transcribe
- **Automatic Cleanup**: Audio files are automatically deleted after transcription
- **Lightweight**: Minimal system resources with efficient processing
- **No Internet Required**: Works completely offline

## How It Works

Speak-Write runs quietly in your system tray and listens for the hotkey combination Ctrl+Shift+0. Here's what happens when you use it:

1. **Press and Hold**: Press Ctrl+Shift+0 to start recording (up to 30 seconds)
2. **Speak**: A small overlay appears showing "Listening..." while you talk
3. **Release**: Let go of the keys to stop recording
4. **Process**: The app shows "Processing" while Whisper transcribes your audio locally
5. **Paste**: Transcribed text is automatically pasted into your active window
6. **Cleanup**: The temporary audio file is immediately deleted

## Privacy and Security

Your privacy is our top priority. Here's how Speak-Write protects your data:

- **Local Processing Only**: All speech recognition happens on your computer using the local Whisper model
- **No Network Traffic**: The application never connects to the internet or external servers
- **Automatic File Deletion**: Audio recordings are stored temporarily and deleted immediately after transcription
- **No Data Collection**: No usage statistics, analytics, or personal data is collected
- **No Cloud Dependencies**: Works completely offline without any cloud services

## Technical Architecture

Speak-Write is built with Python and uses several key components:

- **Audio Capture**: PyAudio for real-time microphone input
- **Speech Recognition**: Faster-Whisper (optimized Whisper implementation) with "tiny" model for speed
- **System Integration**: PyAutoGUI and PyPerclip for seamless text insertion
- **UI**: Minimal Tkinter overlay for user feedback and Pystray for system tray integration
- **Hotkey Management**: Keyboard library for global hotkey detection

The application uses the Whisper "tiny" model running on CPU with int8 optimization for the best balance of speed and accuracy while maintaining low system requirements.

## Quick Start

1. Download the [latest executable](https://github.com/zachtsk/speak-write/releases/tag/v0.1.0)
2. Run the executable - a microphone icon will appear in your system tray
3. Open any application where you want to input text
4. Press and hold Ctrl+Shift+0, speak your message, then release
5. Your transcribed text will be automatically pasted

## Building from Source

### Prerequisites

- **Python 3.8 or higher** (3.9+ recommended for best performance)
- **Pip** package manager
- **Virtual environment** (strongly recommended)
- **Microphone** access permissions
- **Windows** (primary support - Linux/Mac may work but untested)

### Build Steps

1. **Clone the repository**:
```bash
git clone https://github.com/zachtsk/speak-write.git
cd speak-write
```

2. **Set up virtual environment**:
```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On Linux/Mac:
source venv/bin/activate
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

4. **Download Whisper model** (required for offline executable):
```bash
python download_model.py
```

5. **Generate build configuration** (creates spec file from template):
```bash
python update_spec.py
```

6. **Run from source** (for development):
```bash
python src/main.py
```

7. **Build executable**:
```bash
pyinstaller speak-write.spec
```

The executable will be created in the `dist/` directory as a single file with the Whisper model bundled inside (~80MB).

### Development Setup

For development work, you may want to install additional tools:
```bash
pip install -e .  # Install in editable mode
```

### Troubleshooting Build Issues

- **PyAudio installation fails**: You may need to install Microsoft C++ Build Tools
- **Permission errors**: Run terminal as administrator on Windows
- **Missing dependencies**: Ensure all requirements.txt packages are installed
- **Whisper model download**: First run may take time to download the model

## System Requirements

- **Operating System**: Windows 10/11 (primary), Linux/macOS (experimental)
- **RAM**: Minimum 4GB, 8GB recommended
- **Storage**: ~500MB for dependencies and models
- **Microphone**: Any system-compatible microphone
- **Permissions**: Microphone access, keyboard input monitoring

## Contributing

Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests. When contributing:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## Support

If you encounter issues:
1. Check the [Issues page](https://github.com/zachtsk/speak-write/issues) for known problems
2. Create a new issue with detailed information about your problem
3. Include your OS version, Python version, and error messages

## License

This project is licensed under the MIT License - see the LICENSE file for details.
