import os
import glob
import cv2 as cv
import numpy as np
import dlib
from tqdm import tqdm

detector = dlib.get_frontal_face_detector()
sp = dlib.shape_predictor("shape_predictor_5_face_landmarks.dat")

for f in glob.glob('face_align_samples/*'):
    os.remove(f)

aligned_faces = 0
missed_faces = 0

for index, fname in enumerate(tqdm(os.listdir('face_crop_samples'))):
    img = cv.imread(os.path.join("face_crop_samples", fname))
    dets = detector(img, 1)
    faces = dlib.full_object_detections()
    for detection in dets:
        faces.append(sp(img, detection))
    try:
        images = dlib.get_face_chips(img, faces, size=180)
        for image in images:
            aligned_faces += 1
            cv.imwrite(os.path.join('face_align_samples', f'aligned_{str(index).zfill(5)}.png'), image)
    except RuntimeError:
        missed_faces += 1
        print(f'No faces were specified in the faces array for image: {fname}')
        continue

print(f'Faces aligned: {aligned_faces}\nFaces missed: {missed_faces}')