import subprocess


def blur_video(timestamps):
    subprocess.run(["ffmpeg", "-y", "-i", "C:\\Users\\kotta\\Desktop\\Programming\\Python\\FFMPEG\\blurVideo\\files\\input.mp4", "-filter_complex", "[0:v]boxblur=30:enable='between(t,4,10)' [fg]", "-map", "[fg]", "blurred.mp4"])