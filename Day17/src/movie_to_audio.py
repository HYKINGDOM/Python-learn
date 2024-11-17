from moviepy.editor import VideoFileClip


if __name__ == '__main__':

    # 选择视频文件
    # 视频文件路径或文件名
    video_path = r"N:\\视频\\说清英语语法.mp4"

    # 使用VideoFileClip函数创建一个VideoFileClip对象，用于处理视频文件
    video = VideoFileClip(video_path)

    # 使用audio方法从VideoFileClip对象中提取音频
    audio = video.audio

    # 使用write_audiofile方法将提取的音频保存到文件中
    # 音频文件输出路径或文件名
    audio_output_path = "N:\\视频\\audio.wav"
    audio.write_audiofile(audio_output_path)