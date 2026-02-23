import os
import time
import glob
import random

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

if __name__ == "__main__":
    for file_path in sorted(glob.glob("data/test_*.txt")):
        with open(file_path, 'r') as f:
            data = [float(line.strip()) for line in f]
            
        start = time.perf_counter()
        quick_sort(data)
        end = time.perf_counter()
        
        print(f"{os.path.basename(file_path)}: {(end - start) * 1000:.2f} ms")
