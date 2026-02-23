import time
import glob
import os

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))

def run_benchmark():
    for file_path in sorted(glob.glob("data/test_*.txt")):
        with open(file_path, 'r') as f:
            data = [float(line.strip()) for line in f]
            
        start = time.perf_counter()
        merge_sort(data)
        end = time.perf_counter()
        
        print(f"{os.path.basename(file_path)}: {(end - start) * 1000:.2f} ms")

if __name__ == "__main__":
    run_benchmark()
