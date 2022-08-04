import os
import dlib
import glob
import cv2 as cv

def mouthroi():
    detector = dlib.get_frontal_face_detector()
    model = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
    win = dlib.image_window()

    if not os.path.exists("mouth_roi"):
        os.makedirs("mouth_roi")
    for folder in glob.glob("mouth_roi/*"):
        os.remove(folder)
    image_no = 0
    for f in glob.glob(os.path.join("frame_copy", "*.jpg")):
        img = cv.imread(f)
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY) 
        win.clear_overlay()
        win.set_image(img)
        dets = detector(img, 1)
        for d in dets:
            shape = model(img, d)
            xmouthpoints = [shape.part(x).x for x in range(48,67)]
            ymouthpoints = [shape.part(x).y for x in range(48,67)]
            maxx = max(xmouthpoints)
            minx = min(xmouthpoints)
            maxy = max(ymouthpoints)
            miny = min(ymouthpoints)
            pad = 10
            crop_image = img[miny-pad:maxy+pad,minx-pad:maxx+pad]
            # cv.imshow('mouth', crop_image)
            #crop_image=cv.resize(crop_image,(180,180))
            cv.imwrite(os.path.join(f'./mouth_roi/{image_no:04d}.png'), crop_image)
            image_no += 1
            cv.waitKey(0)
            cv.destroyAllWindows()
            win.add_overlay(shape)
        win.add_overlay(dets)