from gtts import gTTS
import os
import platform


def play_voice(text):
    #テキストから音声作成する
    tts = gTTS(text=text, lang='ja')
    voice = '04.mp3'
    tts.save(voice)
    if platform.system() == 'Darwin':
        os.system('open ' + voice)
    else:
        os.system('start ' + voice)
play_voice("もう！ええでしょ")
print("！！作成完了！！")