# Speak-Write

Speak-Write is a fast and simple voice-to-text desktop application leveraging OpenAI's Whisper model.

## Features

- Fast voice recognition
- Efficient transcription using OpenAI's Whisper model
- Transcribe your words using a simple keyboard shortcut (Ctrl+Shift+0)

## Usage
Once you start the application, press "Ctrl+Shift+0" to start recording. Release the keys to stop recording and transcribe the speech to text in whatever text application you have open.

Enjoy typing without typing!

## Building from source

### Prerequisites

- Python 3.8 or above
- Pip
- Virtual environment (recommended)

### Steps

1. Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/speak-write.git
```

2. Navigate into the project directory:
```bash
cd speak-write
```

3. Create a virtual environment (optional, but recommended):
    
```bash 
python -m venv venv
```

4. Activate the virtual environment:

```bash
venv\Scripts\activate
```

5. Install the required dependencies:

```bash 
pip install -r requirements.txt
```

Optionally, to build the .exe file, run the following command:

```bash
pip install -r requirements-dev.txt
```

6. Run PyInstaller to build the .exe file:

```bash 
pyinstaller --onefile --windowed --add-data "assets/megaphone.png;assets" --icon=assets/megaphone.png --name speak-write src/main.py
```

This command will create a one-file executable in the `dist/` directory.

## License
This project is licensed under the terms of the MIT license.