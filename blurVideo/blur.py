import subprocess

def blur_video(timestamps):
    query = ""
    for index, timestamp in enumerate(timestamps):
        if index == 0:
            query = f"[0:v]boxblur=30:enable='between(t,{timestamp[0]},{timestamp[1]})' [fg{index}];"
        else:
            query = query +  f"[fg{index-1}]boxblur=30:enable='between(t,{timestamp[0]},{timestamp[1]})' [fg{index}];"
    subprocess.run(["ffmpeg", "-y", "-i", ".\\blurVideo\\files\\input.mp4", "-filter_complex", query[:-1], "-map", f"[fg{len(timestamps)-1}]", ".\\blurVideo\\files\\blurred.mp4"])