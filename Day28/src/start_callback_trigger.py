from RealtimeSTT import AudioToTextRecorder


def start_callback():
    print("Recording started!")


def stop_callback():
    print("Recording stopped!")


if __name__ == '__main__':
    recorder = AudioToTextRecorder(on_recording_start=start_callback,
                                   on_recording_stop=stop_callback)
