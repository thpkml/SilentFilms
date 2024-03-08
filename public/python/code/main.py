from trimming import videotrimming
from facedetector import*
from facealign import*
from frames_to_video import*
from mouthroi import*
import argparse

parser = argparse.ArgumentParser(description='Example list of options', add_help=True)
parser.add_argument('-1', '--videotrimming', dest='command', action='store_const', const='videotrimming', help='video trimming')
parser.add_argument('-2', '--facedetector', dest='command', action='store_const', const='facedetector', help='face detection')
parser.add_argument('-3', '--facealign', dest='command', action='store_const', const='facealign', help='face alignment')
parser.add_argument('-4', '--facetovideo', dest='command', action='store_const', const='facetovideo', help='converting align frames to video')
parser.add_argument('-5', '--mouthroi', dest='command', action='store_const', const='mouthroi', help='croping mouth region of interest')
parser.add_argument('-6', '--mouthtovideo', dest='command', action='store_const', const='mouthtovideo', help='converting mouth frames to video')

args = parser.parse_args()

if args.command == 'videotrimming':
    videotrimming(input="clip.mp4")
elif args.command == 'facedetector':
    facedetector(invideo="./trim/25.mp4", facedetector="shape_predictor_68_face_landmarks.dat")
elif args.command == 'facealign':
    facealign()
elif args.command == 'facetovideo':
    croptovideo(dir_path="facealign")
elif args.command == 'mouthroi':
    mouthroi()
elif args.command == 'mouthtovideo':
    croptovideo(dir_path="mouth_roi")

# videotrimming(input="makeup.mp4")
# facedetector(invideo="./trim/5.mp4")
# facealign()
# cropivideo(dir_path="facealign")
# mouthroi()
# cropivideo(dir_path="mouth_roi")

# import argparse

# parser = argparse.ArgumentParser(description='Process some integers.')
# parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                     help='an integer for the accumulator')
# parser.add_argument('--sum', dest='accumulate', action='store_const',
#                     const=sum, default=max,
#                     help='sum the integers (default: find the max)')

# args = parser.parse_args()
# print(args.accumulate(args.integers))