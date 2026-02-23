import os
import time
import glob

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

if __name__ == "__main__":
    for file_path in sorted(glob.glob("data/test_*.txt")):
        with open(file_path, 'r') as f:
            data = [float(line.strip()) for line in f]
            
        start = time.perf_counter()
        heap_sort(data)
        end = time.perf_counter()
        
        print(f"{os.path.basename(file_path)}: {(end - start) * 1000:.2f} ms")