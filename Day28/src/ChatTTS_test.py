import ChatTTS
import torch
import soundfile as sf

if __name__ == '__main__':
    chat = ChatTTS.Chat()
    try:
        chat.load(compile=False)  # Set to True for better performance
        print("Model loaded successfully.")
    except Exception as e:
        print(f"Error loading model: {e}")

    texts = ["PUT YOUR 1st TEXT HERE", "PUT YOUR 2nd TEXT HERE"]

    try:
        wavs = chat.infer(texts, stream=True)
        print("type: ",type(wavs))  # 调试信息
        sf.write(f"D:\\project\\output{1}.wav", wavs, 24000)
        print(f"Audio {1} saved successfully.")
    except Exception as e:
        print(f"Error generating audio: {e}")
