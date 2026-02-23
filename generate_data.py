import numpy as np
import os

os.makedirs('data', exist_ok=True)

N = 1_000_000

for i in range(10):
    if i < 5:
        arr = np.random.uniform(-10**6, 10**6, N)
        fmt, suffix = "%f", "float"
    else:
        arr = np.random.randint(-10**6, 10**6, N)
        fmt, suffix = "%d", "int"

    if i == 0: 
        arr.sort()                  
    elif i == 1: 
        arr = np.sort(arr)[::-1]
    
    filename = f"data/test_{i}_{suffix}.txt"
    arr.tofile(filename, sep="\n", format=fmt)
    
    print(f"Đã tạo: {filename}")