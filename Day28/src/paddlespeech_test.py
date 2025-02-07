import os
import wave

import pyaudio
from paddlespeech.cli.asr.infer import ASRExecutor
from paddlespeech.cli.utils import download_and_decompress
from paddlespeech.cli.vector.infer import VectorExecutor

'''

pip install paddlespeech
'''

# 关键词唤醒配置
wakeup_model_url = 'https://paddlespeech.bj.bcebos.com/vector/wakeup_model.tar.gz'
wakeup_model_path = 'wakeup_model'
if not os.path.exists(wakeup_model_path):
    download_and_decompress(wakeup_model_url, wakeup_model_path)

# 初始化语音唤醒执行器
vector_executor = VectorExecutor()
# 关键词文件，这里以 "你好，小度" 为例，可根据需要修改
keyword_file = os.path.join(wakeup_model_path, 'keyword.list')
# 唤醒阈值，可根据实际情况调整
threshold = 0.8

# 初始化语音识别执行器
asr_executor = ASRExecutor()

# 录音配置
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
RECORD_SECONDS = 5  # 录音时长，可根据需要调整
WAVE_OUTPUT_FILENAME = "output.wav"

# 初始化 PyAudio
p = pyaudio.PyAudio()

# 打开音频流
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("开始监听关键词...")

try:
    while True:
        # 读取音频数据
        data = stream.read(CHUNK)
        # 进行关键词检测
        score = vector_executor(wav_file=data,
                                task='wakeup',
                                threshold=threshold,
                                keyword_file=keyword_file)
        if score > threshold:
            print("检测到关键词，开始录音...")
            frames = []
            for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
                data = stream.read(CHUNK)
                frames.append(data)
            print("录音结束，开始进行语音识别...")
            # 保存录音文件
            wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(p.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(frames))
            wf.close()
            # 进行语音识别
            result = asr_executor(audio_file=WAVE_OUTPUT_FILENAME, lang='zh')
            print("语音识别结果: ", result)
            print("继续监听关键词...")

except KeyboardInterrupt:
    print("程序终止")

# 关闭音频流和 PyAudio
stream.stop_stream()
stream.close()
p.terminate()
