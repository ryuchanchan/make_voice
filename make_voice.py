from gtts import gTTS
import os
import platform

language = 'ja'
voice_file = '04.mp3'

def play_voice(text):
    #テキストから音声作成する
    tts = gTTS(text=text, lang=language)
    tts.save(voice_file)
    if platform.system() == 'Darwin':
        os.system('open ' + voice_file)
    else:
        os.system('start ' + voice_file)
play_voice("こんにちわ")
print("！！作成完了！！")