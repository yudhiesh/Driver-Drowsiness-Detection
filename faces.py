import sys
import time 
import numpy as np
import concurrent.futures
import dlib
import os 
import cv2 
import time 


"""
TODO: 
    1) Find the file paths for each label - DONE
    2) Store them in a list - DONE 
    3) Create a function to apply dlib 
    4) Apply dlib and detect the faces in each frame 
    5) Crop out the faces in each frame 
    6) If there is a face store them in a folder in the same directory as a 
       folder called label number_faces


    *Need to rotate images so that the faces are facing vertically*
"""
frames_path = "/Volumes/HDD/frames"
path_HDD = "/Volumes/HDD/Data"
last_file = ["/Volumes/HDD/Data/Fold4_part2"]

def file_last(file):
    for root, directories, files in os.walk(file, topdown=False):
        for file in files:
            if (directories == []): 
                pass
            elif (len(directories) > 3):
                pass
            elif (len(root) == 29):
                pass
            else: 
                for dir in directories:
                    path_vid = os.path.join(root, dir)
                    for r, d, f in os.walk(path_vid, topdown=False):
                        for fe in f:
                            fullPath = r[:32]
                            label = r[-1:]
                            folds = path_vid.replace("/Volumes/HDD/Data/", "")
                            finalPath = os.path.join(frames_path, folds)
                            finalImage = os.path.join(finalPath, fe)
                            fullImagePath = os.path.join(path_vid, fe)
                            try: 
                                if(os.path.exists(fullImagePath) == False):
                                    os.makedirs(fullImagePath)
                                with concurrent.futures.ProcessPoolExecutor() as executor:
                                    executor.map(extractFaces(fullImagePath, finalImage))
                              # extractFaces(fullImagePath, finalImage)
                            except OSError as error:
                                print(error)

                            # full image path has the image from data



def filePath(path):
    for root, directories, files in os.walk(path, topdown=False):
        for file in files:
            if (directories == []): 
                pass
            elif (len(directories) > 3):
                pass
            elif (len(root) == 29):
                pass
            else: 
            # Only want the roots with /Volumes/HDD/Data/Fold1_part1/01
                for dir in directories:
                    path_video = os.path.join(root, dir)
                    for r, d, f in os.walk(path_video, topdown=False):
                        for fe in f:
                            fullPath = r[:32]
                            label = r[-1:]
                            folds = path_video.replace("/Volumes/HDD/Data/", "")
                            finalPath = os.path.join(frames_path, folds)
                            finalImage = os.path.join(finalPath, fe)
                            fullImagePath = os.path.join(path_video, fe)
                            try :
                               if (os.path.exists(finalPath) == False):
                                   os.makedirs(finalPath)
                               with concurrent.futures.ProcessPoolExecutor() as executor:
                                   executor.map(extractFaces(fullImagePath, finalImage))
                              # extractFaces(fullImagePath, finalImage)
                            except OSError as error:
                               print(error)
                             
    sys.exit(0)

def extractFaces(imageTest, savePath):
    tic = time.perf_counter()
    model = "/Users/yudhiesh/Downloads/deep-learning-face-detection/res10_300x300_ssd_iter_140000.caffemodel"
    prototxt = "/Users/yudhiesh/Downloads/deep-learning-face-detection/deploy.prototxt.txt"
    
    net = cv2.dnn.readNet(model, prototxt)
    # load the input image and construct an input blob for the image
    # by resizing to a fixed 300x300 pixels and then normalizing it
    image = cv2.imread(imageTest)
    (h, w) = image.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0,(300, 300), (104.0, 177.0, 123.0))
    print(f'Current file path {imageTest}')
   
# pass the blobs through the network and obtain the predictions
    print("Computing object detections....")
    net.setInput(blob)
    detections = net.forward()
   # Detect face with highest confidence
    for i in range(0, detections.shape[2]):
        box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
        (startX, startY, endX, endY) = box.astype("int")
   
        confidence = detections[0, 0, i, 2]
   
   # If confidence > 0.5, save it as a separate file
        if (confidence > 0.5):
            frame = image[startY:endY, startX:endX]
            rect = dlib.rectangle(startX, startY, endX, endY)
            image = image[startY:endY, startX:endX]
            print(f'Saving image to {savePath}')
            cv2.imwrite(savePath, image)
            toc = time.perf_counter()
            print(f'Time taken {toc - tic:0.4f}')

if __name__ == "__main__":
    file_last("/Volumes/HDD/Data/Fold4_part2/42")
