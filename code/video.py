import os
import cv2
import glob
def cropivideo(dir_path):
    
    if dir_path=="facealign":
        for f in glob.glob("face_align_sample.mp4"):
            os.remove(f)
            #dir_path = "facealign"
        output = 'face_align_sample.mp4'
    elif dir_path=="mouth_roi":
        for f in glob.glob("mouth_roi_sample.mp4"):
            os.remove(f)
        output = 'mouth_roi_sample.mp4'

    ext = '.png'
    shape = 40, 40
    fps = 10
    images = [f for f in os.listdir(dir_path) if f.endswith(ext)]
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(output, fourcc, fps, shape)
    for image in images:
        image_path = os.path.join(dir_path, image)
        image = cv2.imread(image_path)
        resized=cv2.resize(image,shape) 
        video.write(resized)
    video.release()
