import os
import queue
import sys
import numpy as np
import scipy.io.wavfile as wavfile
import sounddevice as sd
import whisper

# Configuration
AUDIO_FILENAME = "temp_recording.wav"
SAMPLE_RATE = 16000  # Whisper works best with 16kHz audio
MODEL_SIZE = "base"  # Options: 'tiny', 'base', 'small', 'medium', 'large'


def record_live_audio(filename, sample_rate=16000):
    """Records audio from the microphone until the user hits Ctrl+C."""
    q = queue.Queue()

    def callback(indata, frames, time, status):
        """This is called for each audio block by sounddevice."""
        if status:
            print(status, file=sys.stderr)
        q.put(indata.copy())

    print("\n" + "=" * 50)
    print(">>> Starting Live Recording...")
    print(">>> Press [Ctrl + C] to STOP recording and start transcribing.")
    print("=" * 50 + "\n")

    audio_data = []
    try:
        # Open the microphone stream
        with sd.InputStream(
            samplerate=sample_rate, channels=1, callback=callback, dtype="int16"
        ):
            while True:
                audio_data.append(q.get())
    except KeyboardInterrupt:
        print("\n\nRecording stopped by user. Processing audio...")

    # Concatenate all recorded blocks and save to a WAV file
    if audio_data:
        recording = np.concatenate(audio_data, axis=0)
        wavfile.write(filename, sample_rate, recording)
        return True
    else:
        print("No audio data recorded.")
        return False


def transcribe_audio(filename, model_name="base"):
    """Loads the Whisper AI model and transcribes the target audio file."""
    if not os.path.exists(filename):
        print(f"Error: The file {filename} does not exist.")
        return

    print(f"Loading AI Whisper Model ('{model_name}'). Please wait...")
    # This will download the model weights automatically on the first run
    model = whisper.load_model(model_name)

    print("Transcribing voice to text...")
    # fp16=False ensures compatibility even if you don't have a dedicated Nvidia GPU
    result = model.transcribe(filename, fp16=False)

    print("\n" + "=" * 50)
    print("FINAL TRANSCRIPTION:")
    print("=" * 50)
    print(result["text"].strip())
    print("=" * 50 + "\n")


if __name__ == "__main__":
    print("Welcome to AI Speech-to-Text Project")
    print("1. Transcribe an existing audio file (.mp3, .wav, etc.)")
    print("2. Record live voice from Microphone and transcribe")

    choice = input("Select an option (1 or 2): ").strip()

    if choice == "1":
        file_path = input(
            "Enter the path to your audio file (e.g., audio.mp3): "
        ).strip()
        transcribe_audio(file_path, model_name=MODEL_SIZE)

    elif choice == "2":
        # Step 1: Record from mic
        if record_live_audio(AUDIO_FILENAME, SAMPLE_RATE):
            # Step 2: Transcribe the temporary recording
            transcribe_audio(AUDIO_FILENAME, model_name=MODEL_SIZE)

            # Clean up the temporary file after transcription
            if os.path.exists(AUDIO_FILENAME):
                os.remove(AUDIO_FILENAME)
    else:
        print("Invalid choice. Exiting program.")