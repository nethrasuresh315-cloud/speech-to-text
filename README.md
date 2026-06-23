# AI-Based Speech-to-Text Project 🎙️🤖

An offline, high-accuracy AI Speech-to-Text application built in Python using OpenAI's open-source **Whisper** model. This project allows users to either transcribe pre-recorded audio files or capture live voice directly from a microphone and instantly convert it into written text.

---

## ✨ Features
* **Two-Way Input:** Transcribe existing audio files (`.mp3`, `.wav`, etc.) or record live audio on the fly.
* **Powered by Whisper AI:** Uses OpenAI's Whisper model for highly accurate, context-aware transcriptions.
* **Fully Offline:** Processing happens locally on your machine—no premium API keys or external cloud subscriptions required.
* **Multilingual Capability:** Whisper automatically detects and transcribes dozens of global languages.

---

## 🛠️ Prerequisites

Before running the project, you must install **FFmpeg** on your operating system, as Whisper relies on it to process audio streams.

### 1. Install FFmpeg
* **Windows** (via Winget): 
```bash
  winget install Gyan.FFmpeg
#Install Python Packages
Install the required dependencies using pip

pip install sounddevice openai-whisper scipy numpy

🚀 How to Run
Clone or download this repository to your local machine.

Open your terminal/command prompt and navigate to the project directory.

Run the main script:
    python app.py

🎮 Using the Application
Upon running the script, you will see a menu with two choices:

Option 1 (Transcribe File): Provide the file path (e.g., sample.mp3 or C:\path\to\audio.wav) to get an instant transcription.

Option 2 (Live Recording): Start speaking immediately into your microphone. When you are done speaking, press Ctrl + C in your terminal to stop recording and initiate the AI transcription.

⚙️ Configuration & Customization
You can change the accuracy and speed performance by opening app.py and adjusting the MODEL_SIZE variable:

        MODEL_SIZE = "base" # Options: 'tiny', 'base', 'small', 'medium', 'large'



📝 License
This project is open-source and available under the MIT License.

### 💡 Tips for your GitHub Repository:
1. **Add a `LICENSE` file:** Choose the MIT License if you want it completely open-source.
2. **Add a `.gitignore` file:** Create a file named `.gitignore` and add `temp_recording.wav` inside it, so your temporary audio recordings don't accidentally get uploaded to GitHub
