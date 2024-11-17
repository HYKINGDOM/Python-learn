import speech_recognition as sr
import os

if __name__ == '__main__':
    # 选择音频文件
    # 音频文件路径或文件名
    audio_path = "N:\\视频\\audio.wav"

    # 创建Recognizer对象，用于处理音频文件
    recognizer = sr.Recognizer()

    # 使用Recognizer对象的record方法读取音频文件
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)

    # 语音识别
    text = recognizer.recognize_google_cloud(audio, language='zh-CN')
    print(text)

    # 清理临时文件
    os.remove(audio_path)
