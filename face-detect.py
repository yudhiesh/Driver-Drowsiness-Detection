import cv2
import numpy as np 
import sys

face_path = "/Users/yudhiesh/Downloads/frontalFace10/haarcascade_frontalface_default.xml"
imgTest = "/Volumes/HDD/Data/Fold1_part1/01/5/00001.jpg"


"""
TODO: 
Does not work on imgs that are rotated as well 
I have to go through the imgs and find any that are not rotated then rotate them 
"""


face_cascade = cv2.CascadeClassifier(face_path)

img = cv2.imread(imgTest )
faces_detected = face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5)
print("[INFO] Found {0} Faces.".format(len(faces_detected)))

for (x, y, w, h) in faces_detected:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    roi_color = img[y:y + h, x:x + w]
    print("[INFO] Object found. Saving locally.")
    cv2.imwrite(str(w) + str(h) + '_faces.jpg', roi_color)

status = cv2.imwrite('/Users/yudhiesh/Downloads/deep-learning-face-detection/faces_detected1.jpg', img)
print("[INFO] Image faces_detected.jpg written to filesystem: ", status)
sys.exit()
