import os
import time
import glob
import numpy as np

if __name__ == "__main__":
    for file_path in sorted(glob.glob("data/*.txt")):
        data = np.fromfile(file_path, sep="\n")
        
        start = time.perf_counter()
        np.sort(data) 
        end = time.perf_counter()
        
        print(f"{os.path.basename(file_path)}: {(end - start) * 1000:.2f} ms")