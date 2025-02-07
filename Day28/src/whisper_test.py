import whisper

'''
pip install git+https://github.com/openai/whisper.git

'''

# 加载模型
model = whisper.load_model("base")

# 进行语音识别
result = model.transcribe("your_audio_file.wav", language='zh')
print("识别结果: " + result["text"])