from trimming import videotrimming
from facedetector import*
from facealign import*
from frames_to_video import*
from mouthroi import*
import argparse
import os


parser = argparse.ArgumentParser(description='Example list of options', add_help=True)
parser.add_argument('-1', '--videotrimming', dest='command', action='store_const', const='videotrimming', help='video trimming')
parser.add_argument('-2', '--facedetector', dest='command', action='store_const', const='facedetector', help='face detection')
parser.add_argument('-3', '--facealign', dest='command', action='store_const', const='facealign', help='face alignment')
parser.add_argument('-4', '--facetovideo', dest='command', action='store_const', const='facetovideo', help='converting align frames to video')
parser.add_argument('-5', '--mouthroi', dest='command', action='store_const', const='mouthroi', help='croping mouth region of interest')
parser.add_argument('-6', '--mouthtovideo', dest='command', action='store_const', const='mouthtovideo', help='converting mouth frames to video')


args = parser.parse_args()

_location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

input_path = os.path.abspath(os.path.join(_location, 'makeup.mp4'))
face_detect_vid = os.path.abspath(os.path.join(_location, 'trim', '5.mp4'))
face_detector = os.path.abspath(os.path.join(_location, 'shape_predictor_68_face_landmarks.dat'))

if args.command == 'videotrimming':
    videotrimming(input=input_path)
elif args.command == 'facedetector':
    facedetector(invideo=face_detect_vid, facedetector=face_detector)
elif args.command == 'facealign':
    facealign()
elif args.command == 'facetovideo':
    croptovideo(dir_path="facealign")
elif args.command == 'mouthroi':
    mouthroi()
elif args.command == 'mouthtovideo':
    croptovideo(dir_path="mouth_roi")


# step1 = videotrimming(input="makeup.mp4")
# step2 = facedetector(invideo="./trim/5.mp4")
# step3 = facealign()
# step4 = croptovideo(dir_path="facealign")
# step5 = mouthroi()
# step6 = croptovideo(dir_path="mouth_roi")