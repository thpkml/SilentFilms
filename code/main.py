from trimming import videotrimming
from facedetector import*
from facealign import*
from facealignvideo import*
from mouthroi import*

videotrimming(input="abc.mp4")
facedetector(invideo="./trim/16.mp4")
facealign()
cropivideo(dir_path="facealign")
mouthroi()
cropivideo(dir_path="mouth_roi")

