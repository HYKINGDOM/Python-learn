import speech_recognition as sr


'''
pip install SpeechRecognition
pip install pocketsphinx
'''


# 创建一个 Recognizer 对象
r = sr.Recognizer()

# 使用麦克风作为音频源
with sr.Microphone() as source:
    print("请说话...")
    audio = r.listen(source)

try:
    # 使用 PocketSphinx 进行语音识别
    text = r.recognize_sphinx(audio, language='zh-CN')
    print("识别结果: " + text)
except sr.UnknownValueError:
    print("无法识别语音")
except sr.RequestError as e:
    print(f"发生错误; {e}")