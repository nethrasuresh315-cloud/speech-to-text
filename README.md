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
