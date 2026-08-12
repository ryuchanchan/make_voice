# Python gTTS Japanese Voice Generator

A simple Python program that converts Japanese text into speech
using gTTS and automatically plays the generated MP3 file.

日本語テキストを音声に変換してMP3として保存し、
Mac / Windowsで自動再生するシンプルなPythonプログラムです。

## ✨ Features

* Convert Japanese text to speech
* Generate MP3 audio files
* Automatic audio playback
* Supports macOS and Windows
* Simple and beginner-friendly Python code

## 🛠️ Requirements

* Python 3
* gTTS
* Internet connection

## 📦 Installation

Install gTTS with pip:

```bash
pip install gTTS
```

## 🚀 Usage

Run the Python script:

```bash
python main.py
```

You can change the text by modifying:

```python
play_voice("もう！ええでしょ")
```

For example:

```python
play_voice("Hello!")
```

or:

```python
play_voice("こんにちは。これはPythonで作った音声です。")
```

## 💻 Code

```python
from gtts import gTTS
import os
import platform


def play_voice(text):
    # Convert text to speech
    tts = gTTS(text=text, lang='ja')

    voice = '04.mp3'
    tts.save(voice)

    # Play the generated audio
    if platform.system() == 'Darwin':
        os.system('open ' + voice)
    else:
        os.system('start ' + voice)


play_voice("もう！ええでしょ")

print("Voice generation completed!")
```

## 🔄 How It Works

```text
Japanese Text
      ↓
     gTTS
      ↓
Text-to-Speech
      ↓
   *.mp3
      ↓
Automatic Playback
```

The program:

1. Receives Japanese text.
2. Sends the text to gTTS.
3. Generates Japanese speech.
4. Saves the speech as `04.mp3`.
5. Automatically opens the audio file.

## 🖥️ Supported Platforms

### macOS

Uses the macOS `open` command to play the generated MP3.

### Windows

Uses the Windows `start` command to open the generated MP3.

## ⚠️ Notes

gTTS requires an internet connection because it uses Google's text-to-speech service.

The generated file is always saved as:

```text
*.mp3
```

Running the program again will overwrite the previous `04.mp3`.

## 💡 Possible Applications

This project can be used as a simple voice-generation tool for:

* Python projects
* DIY electronics
* Arduino projects
* DFPlayer Mini projects
* Raspberry Pi projects
* Interactive devices
* Electronic instruments
* Voice-enabled DIY projects

For example, generated MP3 files can be copied to a microSD card and used with a **DFPlayer Mini** in an Arduino project.

## 📚 Learning Purpose

This project is also useful for learning:

* Python functions
* Text-to-Speech
* File handling
* MP3 generation
* Operating system detection
* Basic automation

## 📜 License

This project is provided for educational and personal use.