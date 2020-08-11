import os 
import time 
import sys
import concurrent.futures

path_HDD = "/Volumes/HDD/frames"

#os.rename(r'file path\OLD file name.file type',r'file path\NEW file name.file type')

list_rename = ["/Volumes/HDD/frames/Fold4_part2/44", "/Volumes/HDD/frames/Fold4_part2/46", "/Volumes/HDD/frames/Fold5_part2/58", "/Volumes/HDD/frames/Fold5_part2/57","/Volumes/HDD/frames/Fold5_part2/55", "/Volumes/HDD/frames/Fold5_part2/57" , "/Volumes/HDD/frames/Fold5_part2/56", "/Volumes/HDD/frames/Fold5_part1/54", "/Volumes/HDD/frames/Fold5_part1/53", "/Volumes/HDD/frames/Fold5_part1/52", "/Volumes/HDD/frames/Fold5_part1/51" , "/Volumes/HDD/frames/Fold5_part1/50", "/Volumes/HDD/frames/Fold1_part2/12", "/Volumes/HDD/frames/Fold1_part2/11", "/Volumes/HDD/frames/Fold1_part2/10", "/Volumes/HDD/frames/Fold1_part2/9", "/Volumes/HDD/frames/Fold1_part2/8", "/Volumes/HDD/frames/Fold1_part2/7", "/Volumes/HDD/frames/Fold4_part1/37", "/Volumes/HDD/frames/Fold2_part2/24", "/Volumes/HDD/frames/Fold2_part2/22", "/Volumes/HDD/frames/Fold2_part2/21", "/Volumes/HDD/frames/Fold2_part2/20", "/Volumes/HDD/frames/Fold2_part2/19", "/Volumes/HDD/frames/Fold3_part1/29", "/Volumes/HDD/frames/Fold3_part1/28", "/Volumes/HDD/frames/Fold3_part1/27", "/Volumes/HDD/frames/Fold3_part1/26", "/Volumes/HDD/frames/Fold3_part1/25","/Volumes/HDD/frames/Fold3_part2/35", "/Volumes/HDD/frames/Fold3_part2/34", "/Volumes/HDD/frames/Fold3_part2/31", "/Volumes/HDD/frames/Fold2_part1/18", "/Volumes/HDD/frames/Fold2_part1/17", "/Volumes/HDD/frames/Fold2_part1/16", "/Volumes/HDD/frames/Fold2_part1/15", "/Volumes/HDD/frames/Fold2_part1/14", "/Volumes/HDD/frames/Fold2_part1/13"]


def file_last(file):
    for root, directories, files in os.walk(file, topdown=False):
        if(len(root) == 36 or len(root) == 37):
            for file in files:
                if(len(root) == 36):
                    name1 = root[-4:-2]
                    img_new1 = name1 + file
                    img_final1 = os.path.join(root, img_new1)
                    ori = os.path.join(root, file)
                    print(f'Current dir {ori}')
                    print(f'Saving to {img_final1}')
                    os.rename(ori, img_final1)
                elif(len(root) == 37):
                    name2 = root[-5:-3]
                    img_new2 = name2 + file
                    img_final2 = os.path.join(root, img_new2)
                    ori2 = os.path.join(root, file)
                    print(f'Current dir {ori2}')
                    print(f'Saving to {img_final2}')
                    os.rename(ori2, img_final2)

        else:
            continue
    print("DONE!")
    sys.exit(0)







if __name__ == "__main__":
    try :
        with concurrent.futures.ProcessPoolExecutor():
            file_last(path_HDD)
    except OSError as error:
        print(error)

