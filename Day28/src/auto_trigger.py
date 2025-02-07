from RealtimeSTT import AudioToTextRecorder


def process_text(text):
    print("auto print: ", text)


if __name__ == '__main__':
    recorder = AudioToTextRecorder(language='zh')

    while True:
        recorder.text(process_text)
