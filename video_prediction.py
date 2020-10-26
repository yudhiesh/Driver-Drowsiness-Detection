from tensorflow.keras.models import load_model 
from collections import deque 

import numpy as np 
import pickle
import cv2


def video_prediction(path_to_sample_video, path_to_output):
    classes_ = ["0", "10", "5"]
    Q = deque(maxlen=128)
    model = load_model("/Users/yudhiesh/Downloads/best_model_2.h5")
    vs = cv2.VideoCapture(path_to_sample_video)
    writer = None
    (W, H) = (None, None)
    # loop over frames from the video file stream
    while True:
        # read the next frame from the file
        (grabbed, frame) = vs.read()
        # if the frame was not grabbed, then we have reached the end
        # of the stream
        if not grabbed:
            break
        # if the frame dimensions are empty, grab them
        if W is None or H is None:
            (H, W) = frame.shape[:2]



        output = frame.copy()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.resize(frame, (224, 224)).astype("float32")
        preds = model.predict(np.expand_dims(frame, axis=0))[0]
        Q.append(preds)
        # perform prediction averaging over the current history of
        # previous predictions
        results = np.array(Q).mean(axis=0)
        i = np.argmax(results)
        label = classes_[i]# draw the activity on the output frame
        text = "Awareness Level: {}".format(label)
        cv2.putText(output, text, (35, 50), cv2.FONT_HERSHEY_SIMPLEX,
            1.25, (0, 255, 0), 5)
        # check if the video writer is None
        if writer is None:
            # initialize our video writer
            fourcc = cv2.VideoWriter_fourcc(*"MJPG")
            writer = cv2.VideoWriter(path_to_output, fourcc, 30,
                (W, H), True)
        # write the output frame to disk
        writer.write(output)
        # show the output image
        cv2.imshow("Output", output)
        key = cv2.waitKey(1) & 0xFF
        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break
    # release the file pointers
    print("[INFO] cleaning up...")
    writer.release()
    vs.release()

if __name__ == "__main__":
    video_prediction(path_to_sample_video="/Volumes/HDD/video/10/10\ copy\ 11.mov", path_to_output ="/Users/yudhiesh/Driver_Drowsiness_Detection/frame.av1")
    
