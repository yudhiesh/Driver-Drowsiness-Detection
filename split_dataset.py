import splitfolders 
import concurrent.futures


from tqdm import tqdm 
if __name__ == "__main__":
    input = "/Volumes/HDD/frames_final_all"
    output = "/Volumes/HDD/frames_split"
    with concurrent.futures.ProcessPoolExecutor():
        tqdm(splitfolders.ratio(input, output, seed=42, ratio=(.9, .05, .05), group_prefix=None))

    
