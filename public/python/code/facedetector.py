from fileinput import filename
import dlib 
import cv2 as cv
#import sys
import os
#import pdb
import copy
import glob

def facedetector(invideo, facedetector):

    if not os.path.exists("frame_copy"):
        os.makedirs("frame_copy")

    files = [file for file in glob.glob("frame_copy/*")]
    for file in files:
        os.remove(file)

    cap = cv.VideoCapture(invideo)
    #cap = cv.VideoCapture(0)
    detector = dlib.get_frontal_face_detector()
    model = dlib.shape_predictor(facedetector)
    image_no=0

    while(cap.isOpened()):
        ret, frame = cap.read()   
        #frame = cv.resize(frame,(380,240))
        # cv.imshow("video", frame)
        if ret == False:
            break
        gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        frame_copy = copy.copy(gray)
        faces = detector(gray,1)
        

        for face in faces:
            x1 = face.left()
            y1 = face.top()
            x2 = face.right()
            y2 = face.bottom()
        
            landmarks = model(gray, face)
            for i in range(0, 68):
                x = landmarks.part(i).x
                y = landmarks.part(i).y
                cv.circle(frame, (x, y), 1, (0, 0, 255), -1)
            cv.rectangle(frame, (x1, y1), (x2,y2), (0, 255, 0), 3)
        
        # cropped_image = frame[y1:y2, x1:x2] 
        # cv.imshow("cropped", cropped_image)
        # cropped_image=cv.resize(cropped_image,(36,36))
        # cv.imwrite(f'./frame/{image_no:04d}.jpg', cropped_image)
        #delete the foder content
            copy_image=frame_copy[y1:y2, x1:x2]
            copy_image=cv.resize(copy_image,(180,180))
            cv.imwrite(f"./frame_copy/{image_no:04d}.jpg", copy_image)
            image_no+=1

        #pdb.set_trace()
        cv.imshow("Detection", frame)
        if cv.waitKey(10) & 0xFF == ord('q'):
            break
    

    cap.release()
    cv.destroyAllWindows()



