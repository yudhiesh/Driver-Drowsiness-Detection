import cv2
import time 
import os
import argparse
import sys
path_HDD = "/Volumes/HDD/Data"

"""
TODO : 
    1) It is creating a new folder for each frame need to make it save into a single folder instead .
    2) It is moving the video files into the sub dir /10

""" 

def files(path):
    """
    Function to get the files and add them to a list 
    Args: 
        path: path of the file 
    Not sure what is DS_Store but I do not need it
    """
    for root, directories, files in os.walk(path, topdown=False):
        for name in files:
            file_path = os.path.join(root, name)
            if (name == ".DS_Store"):
                continue 
            else: 
                category = name.split(".")[0]
                # Category returns the video category 
                try: 
                    print("Reading from " + file_path)
                    print("Category:" + category)
                    print("Writing to " + root)
                    video_to_frames(file_path, category, root)
                except:
                    sys.exit("Unable to extract the frames from the video!")
"""
Root : /Volumes/HDD/Data/Fold1_part1/01/
Category : Label of the video 
File path : 
"""
 
        
def video_to_frames(input_loc, label,output_loc):
    """Function to extract frames from input video file
    and save them as separate frames in an output directory.
    Args:
        input_loc: Input video file.
        output_loc: Output directory to save the frames.
    Returns:
        None
    """
    #Checking if the file exists before creating it 
    pathFrame = os.path.join(output_loc, label) 
    if (os.path.exists(pathFrame)):
        pass
    else:
        try:
            os.mkdir(pathFrame) 
            print("Directory '%s' created" %pathFrame) 
        except IOError:
            print("Unable to create the new directory")
            sys.exit()
        
    # Log the time
    time_start = time.time()
    # Start capturing the feed
    cap = cv2.VideoCapture(input_loc)
    # Find the number of frames
    video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
    print ("Number of frames: ", video_length)
    count = 0
    print ("Converting video..\n")
    # Start converting the video
    while cap.isOpened():
        # Extract the frame
        ret, frame = cap.read()
        # Write the results back to output location.
        cv2.imwrite(pathFrame + "/%#05d.jpg" % (count+1), frame)
        # extract a frame every 5 seconds 
        count = count + 5
        # If there are no more frames left
        if (count > (video_length-1)):
            # Log the time again
            time_end = time.time()
            # Release the feed
            cap.release()
            # Print stats
            print ("Done extracting frames.\n%d frames extracted" % count)
            print ("It took %d seconds forconversion." % (time_end-time_start))
            break

if __name__=="__main__":
    files(path_HDD)
