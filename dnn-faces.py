import numpy as np
import dlib 
import sys
import argparse
import cv2
"""
TODO: 
    Done with cropping the faces out 
    Now need to scale it to work on the entire folder

"""

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-c", "--confidence", type=float, default=0.5,
                help="minimum probability to filter weak detections")
args = vars(ap.parse_args())
print("Loading model....")
# load our serialized model from disk
print("[INFO] loading model...")


model = "/Users/yudhiesh/Downloads/deep-learning-face-detection/res10_300x300_ssd_iter_140000.caffemodel"

prototxt = "/Users/yudhiesh/Downloads/deep-learning-face-detection/deploy.prototxt.txt"
imageTest = "/Volumes/HDD/Data/Fold4_part2/42/5/18066.jpg"

net = cv2.dnn.readNet(model, prototxt)
# load the input image and construct an input blob for the image
# by resizing to a fixed 300x300 pixels and then normalizing it
image = cv2.imread(imageTest)
(h, w) = image.shape[:2]
blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0,
                             (300, 300), (104.0, 177.0, 123.0))

# pass the blobs throught the network and obtain the predictions
print("Computing object detections....")
net.setInput(blob)
detections = net.forward()
# Detect face with highest confidence
box = detections[0, 0, 0, 3:7] * np.array([w, h, w, h])

        # Set coordinate
(startX, startY, endX, endY) = box.astype("int")
rect = dlib.rectangle(startX, startY, endX, endY)
image = image[startY:endY, startX:endX]
cv2.imwrite('/Users/yudhiesh/Downloads/deep-learning-face-detection/faces_detected2.jpg', image)
sys.exit()


# show the output image
