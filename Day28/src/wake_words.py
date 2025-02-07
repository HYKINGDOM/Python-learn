from RealtimeSTT import AudioToTextRecorder

if __name__ == '__main__':
    recorder = AudioToTextRecorder(wake_words="jarvis",language='zh')
    print('Say "Jarvis" to start recording.')
    print(recorder.text())
