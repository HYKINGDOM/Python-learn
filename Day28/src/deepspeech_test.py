import deepspeech
import numpy as np
import pyaudio

'''
pip install deepspeech

'''


# 加载模型和语言模型
model_file_path = 'deepspeech-0.9.3-models.pbmm'
scorer_file_path = 'deepspeech-0.9.3-models.scorer'
model = deepspeech.Model(model_file_path)
model.enableExternalScorer(scorer_file_path)

# 初始化 PyAudio
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
stream.start_stream()

print("请说话...")

buffer = []
try:
    while True:
        data = stream.read(1024)
        buffer.append(data)
        audio_data = np.frombuffer(b''.join(buffer), dtype=np.int16)
        text = model.stt(audio_data)
        print("实时识别结果: " + text)
except KeyboardInterrupt:
    print("停止录制")

stream.stop_stream()
stream.close()
p.terminate()