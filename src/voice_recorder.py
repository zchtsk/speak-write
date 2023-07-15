import os
import tempfile
import time
import wave

from src.gui_overlay import Overlay
import pyaudio as pyaudio
from faster_whisper import WhisperModel


class VoiceRecorder:
    """A class for recording and transcribing audio."""

    def __init__(self):
        """Initialize the voice recorder."""
        self.is_recording = False
        self.audio = pyaudio.PyAudio()
        self.frames = []
        self.file_path = None

    def record_audio(self):
        """Record audio for up to 30 seconds."""
        stream = self.audio.open(format=pyaudio.paInt16,
                                 channels=1,
                                 rate=44100,
                                 input=True,
                                 frames_per_buffer=1024)
        with Overlay(txt="Listening..."):
            start_time = time.time()
            while self.is_recording:
                data = stream.read(1024)
                self.frames.append(data)
                if time.time() - start_time >= 30:
                    self.stop_recording()

        stream.stop_stream()
        stream.close()

    def start_recording(self):
        """Start recording audio."""
        if not self.is_recording:
            self.is_recording = True
            self.file_path = os.path.join(tempfile.gettempdir(), 'audio_output.wav')
            print(f"Writing to : {self.file_path}")
            self.record_audio()

    def stop_recording(self):
        """Stop recording audio and save it to a file."""
        if self.is_recording:
            self.is_recording = False
            self.save_audio()

    def save_audio(self):
        """Save the recorded audio to a file."""
        wave_file = wave.open(self.file_path, 'wb')
        wave_file.setnchannels(1)
        wave_file.setsampwidth(self.audio.get_sample_size(pyaudio.paInt16))
        wave_file.setframerate(44100)
        wave_file.writeframes(b''.join(self.frames))
        wave_file.close()
        self.frames = []

    def transcribe_audio(self):
        """Transcribe the recorded audio using the Faster Whisper ASR model."""
        # Load the Faster Whisper ASR model
        model = WhisperModel("base", device="tiny", compute_type="int8")
        segments, info = model.transcribe(self.file_path, beam_size=5)
        # Combine the transcriptions from all segments
        transcription = " ".join(segment.text for segment in segments)
        return transcription

    def clean_up(self):
        """Remove the recorded audio file."""
        if self.file_path:
            try:
                os.remove(self.file_path)
            except:
                pass
