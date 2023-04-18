import cv2 as cv
#from PIL import Image
import dlib
import glob
from tqdm import tqdm
import os

def facealign():

    detector = dlib.get_frontal_face_detector()
    sp = dlib.shape_predictor("shape_predictor_5_face_landmarks.dat")

    if not os.path.exists("facealign"):
        os.makedirs("facealign")
    for f in glob.glob("facealign/*"):
        os.remove(f)
    aligned_faces = 0
    missed_faces = 0
    for index, fname in enumerate(tqdm(os.listdir('frame_copy'))):
        img = cv.imread(os.path.join("frame_copy", fname))
        dets = detector(img, 1)
        faces = dlib.full_object_detections()
        for detection in dets:
            faces.append(sp(img, detection))
    # window = dlib.image_window()
            images = dlib.get_face_chips(img, faces, size=160)
            for image in images:
                aligned_faces += 1
                cv.imwrite(os.path.join('facealign', f'aligned_{str(index).zfill(5)}.png'), image)
            missed_faces += 1
            print(f'No faces were specified in the faces array for image: {fname}')
            continue
    print(f'Faces aligned: {aligned_faces}\nFaces missed: {missed_faces}')