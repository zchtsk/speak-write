import os
import sys
import time
from queue import Queue
from threading import Thread

import keyboard as keyboard
import pyautogui as pyautogui
import pyperclip as pyperclip
import pystray as pystray
from PIL import Image

from src.gui_overlay import Overlay
from src.voice_recorder import VoiceRecorder


def on_click(icon, item):
    icon.stop()
    sys.exit()


def on_hotkey_pressed(vr, overlay_queue):
    print("Hotkey pressed: Start recording")
    vr.start_recording()


def on_hotkey_released(vr, overlay_queue):
    print("Hotkey released: Stop recording and transcribe")
    vr.stop_recording()
    
    original_clipboard = None
    try:
        original_clipboard = pyperclip.paste()
    except:
        pass
    
    with Overlay(txt="Processing"):
        transcription = vr.transcribe_audio()
        transcription = transcription.strip()
        vr.clean_up()

    if transcription:
        print(f"Transcription: {transcription}")
        
        pyautogui.keyUp('ctrl')
        pyautogui.keyUp('shift')
        pyautogui.keyUp('alt')
        pyautogui.keyUp('win')
        time.sleep(0.1)
        
        pyperclip.copy(transcription)
        time.sleep(0.1)
        
        pyautogui.keyDown('ctrl')
        pyautogui.press('v')
        pyautogui.keyUp('ctrl')
        
        # Ensure clean keyboard state after pasting
        time.sleep(0.1)
        pyautogui.keyUp('ctrl')
        pyautogui.keyUp('shift')
        pyautogui.keyUp('alt')
        pyautogui.keyUp('win')
        
        def restore_clipboard():
            time.sleep(0.5)
            if original_clipboard is not None:
                try:
                    pyperclip.copy(original_clipboard)
                except:
                    pass
        
        import threading
        threading.Thread(target=restore_clipboard, daemon=True).start()

def keyboard_event_handler(vr, overlay_queue):
    keyboard.add_hotkey("ctrl+shift+0", on_hotkey_pressed, args=(vr, overlay_queue), suppress=False,
                        trigger_on_release=False)
    keyboard.add_hotkey("ctrl+shift+0", on_hotkey_released, args=(vr, overlay_queue), suppress=True,
                        trigger_on_release=True)

    # Keep the script running
    while True:
        time.sleep(1)


def main():
    vr = VoiceRecorder()

    # Create an overlay_queue to manage overlay updates
    overlay_queue = Queue()

    # Launch the keyboard_event_handler in a separate thread
    keyboard_thread = Thread(target=keyboard_event_handler, args=(vr, overlay_queue), daemon=True)
    keyboard_thread.daemon = True
    keyboard_thread.start()

    icon_path = os.path.join(sys._MEIPASS, "assets/megaphone.png") if hasattr(sys, '_MEIPASS') else "assets/megaphone.png"
    image = Image.open(icon_path)

    menu = (pystray.MenuItem("Exit", on_click),)
    icon = pystray.Icon("name", image, "Speak-Write", menu)

    icon.run()


if __name__ == "__main__":
    main()