try:
    # 尝试导入 RealtimeSTT 模块中的 AudioToTextRecorder 类
    from RealtimeSTT import AudioToTextRecorder
except ImportError:
    # 若导入失败，提示用户该模块未安装，并告知使用 pip 进行安装
    print("'RealtimeSTT' 模块未安装，请使用 pip 进行安装。")
    import sys
    # 退出程序
    sys.exit(1)

def record_audio():
    # 创建 AudioToTextRecorder 类的实例
    recorder = AudioToTextRecorder(language='zh')
    try:
        # 开始录制音频并进行实时语音转文字
        recorder.start()
        # 提示用户按回车键停止录制
        input("按回车键停止录制...")
        # 停止录制
        recorder.stop()
        # 返回录制音频的文字转录结果
        return recorder.text()
    except Exception as e:
        # 若录制过程中出现异常，打印错误信息
        print(f"录制过程中出现错误: {e}")
        return None

if __name__ == '__main__':
    # 调用 record_audio 函数进行录制并获取转录结果
    transcription = record_audio()
    if transcription:
        # 若转录结果不为空，打印转录结果
        print("转录结果: ", transcription)