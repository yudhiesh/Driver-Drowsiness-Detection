import sys
import cv2
import imghdr
import os
import glob 


def remove_img():
    hdd = ["/Volumes/HDD/frames_split/val/0", "/Volumes/HDD/frames_split/val/5", "/Volumes/HDD/frames_split/val/10","/Volumes/HDD/frames_split/train/0", "/Volumes/HDD/frames_split/train/5", "/Volumes/HDD/frames_split/train/10", "/Volumes/HDD/frames_split/test/0", "/Volumes/HDD/frames_split/test/5", "/Volumes/HDD/frames_split/test/10"]
    count = 0
    for folder in hdd:
        print(f"Current directory {folder}")
        for roots, directories, files in os.walk(folder, topdown=False):
            for file in files:
                image_path = os.path.join(folder, file)
                image = cv2.imread(image_path)
                img_type = imghdr.what(image_path)
                if img_type != "jpeg":

                    print(f"[INFO] {image_path} is INVALID! Image type : {str(img_type)}")
                    print(f"Removing {image_path}!")
                    os.remove(image_path)
                    count += 1
                    print(f"Invalid images count {count}")

    sys.exit(0)
                    


if __name__ == "__main__":
    remove_img()    
