import os
import cv2 as cv
#import pdb
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import glob


# calculating duration
def videotrimming(input):
    
    video=cv.VideoCapture(input)
    fps=video.get(cv.CAP_PROP_FPS)
    frame_count = video.get(cv.CAP_PROP_FRAME_COUNT)
    duration=int(frame_count/fps)

    if not os.path.exists("trim"):
        os.makedirs("trim")
    files = [file for file in glob.glob("trim/*")]
    for file in files:
        os.remove(file)

# triming the video 
    first = 0
    last = 5
    targetname = 1
    while last <= duration:
        trim = ffmpeg_extract_subclip(f"{input}", first, last, targetname=os.path.join('Trim',f"{targetname}.mp4"))
        first =last
        last += 5
        targetname += 1









