import os

import cv2
import imagehash
from PIL import Image


def extract_keyframes(video_path, frame_interval=10):
    vidcap = cv2.VideoCapture(video_path)
    success, image = vidcap.read()
    frames = []
    count = 0
    while success:
        if count % frame_interval == 0:
            frames.append(image)
        success, image = vidcap.read()
        count += 1
    return frames


def hash_frame(frame):
    pil_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    return imagehash.average_hash(pil_image)


def get_video_hashes(video_path, frame_interval=10):
    keyframes = extract_keyframes(video_path, frame_interval)
    return [hash_frame(frame) for frame in keyframes]


def compare_hashes(hash_list1, hash_list2, threshold=5):
    matches = 0
    for hash1 in hash_list1:
        for hash2 in hash_list2:
            if hash1 - hash2 < threshold:
                matches += 1
    return matches


def find_duplicates(video_paths, frame_interval=10, threshold=5):
    video_hashes = {}
    for video in video_paths:
        video_hashes[video] = get_video_hashes(video, frame_interval)

    duplicates = []
    for i, video1 in enumerate(video_paths):
        for video2 in video_paths[i + 1:]:
            if compare_hashes(video_hashes[video1], video_hashes[video2], threshold) > 0:
                duplicates.append((video1, video2))
    return duplicates

if __name__ == '__main__':
    # 使用示例
    video_dir = "D:\\video"
    video_files = [os.path.join(video_dir, f) for f in os.listdir(video_dir) if f.endswith(".mp4")]
    duplicates = find_duplicates(video_files)

    for dup in duplicates:
        print(f"Duplicate videos: {dup[0]} and {dup[1]}")
