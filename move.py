import shutil
import os 
import time 
import sys
import concurrent.futures

path_HDD = "/Volumes/HDD/frames/"
path_10 = "/Volumes/HDD/frames_final/10"
path_0 = "/Volumes/HDD/frames_final/0"
path_5 = "/Volumes/HDD/frames_final/5"

def move(path):
    for root, files, directory in os.walk(path, topdown=False):
            if(len(root) == 36 or len(root) == 37):
                if(len(root) == 36 and int(root[-1]) == 0):
                    for r, d, f in os.walk(root, topdown=False):
                        for fi in f:
                            file_path = os.path.join(r, fi)
                            try:
                                shutil.copy(file_path, path_0)
                            except OSError as error:
                                print(error)
                                break
                elif(len(root) == 36 and int(root[-1]) == 5):
                    for r, d, f in os.walk(root, topdown=False):
                        for fi in f:
                            file_path = os.path.join(r, fi)
                            try:
                                shutil.copy(file_path, path_5)
                            except OSError as error:
                                print(error)
                                break
                elif(len(root) == 37 and int(root[-2:]) == 10):
                    for r, d, f in os.walk(root, topdown=False):
                        for fi in f:
                            file_path = os.path.join(r, fi)
                            try:
                                shutil.copy(file_path, path_10)
                            except OSError as error:
                                print(error)
                                break
    print("DONE")
    sys.exit(0)


if __name__ == "__main__":
    try :
        with concurrent.futures.ProcessPoolExecutor():
            move(path_HDD)
    except OSError as error:
        print(error)

