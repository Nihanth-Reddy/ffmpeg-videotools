import subprocess
import time

def blur_video(timestamps: list, file_path: str):
    """
    Args:
        timestamps: List of video segment timestamps which needs to be blurred
        file_path: Path of the input video
    """
    query = ""
    
    # Generates the query by iterating through the list of timestamps
    for index, timestamp in enumerate(timestamps):
        if index == 0:
            query = f"[0:v]boxblur=30:enable='between(t,{timestamp[0]},{timestamp[1]})' [fg{index}];"
        else:
            query = query +  f"[fg{index-1}]boxblur=30:enable='between(t,{timestamp[0]},{timestamp[1]})' [fg{index}];"
    
    # Runs the FFMPEG command with filter query generated
    subprocess.run(["ffmpeg", "-y", "-i", file_path, "-filter_complex", query[:-1], "-map", f"[fg{len(timestamps)-1}]", f".\\blurVideo\\files\\blurred{int(time.time())}.mp4"])
