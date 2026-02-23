# 📊 Sorting Algorithms Benchmark

Hi there! 👋 Welcome to my coursework project for Data Structures and Algorithms. 

I built this project to see how classic sorting algorithms actually perform in practice when thrown a massive amount of data. I implemented several algorithms from scratch and benchmarked them against the highly optimized built-in sorting functions in Python (NumPy) and C++.

## 💡 What's in the Benchmark?
To get a fair comparison, I generated 10 different datasets, each packed with 1,000,000 elements. Half of them are integers, and the other half are floats. 

To make things interesting, the data isn't just random. I tested them under different scenarios:
- Array 1: Already sorted (ascending) - the best-case scenario.
- Array 2: Reverse sorted (descending) - the classic worst-case trap.
- Arrays 3 to 10: Completely random elements.

Algorithms tested:
1. Quick Sort
2. Heap Sort
3. Merge Sort
4. Python's `numpy.sort()` 
5. C++'s `std::sort()`

## 📁 Repository Structure
Here's a quick map of the project:

- `data/`: The generated 1M-element datasets will be saved here. 
- `src/`: Source code directory.
  - `generate_data.py`: Script to generate the test datasets.
  - `quick_sort.py`: Custom implementation and benchmark for Quick Sort.
  - `heap_sort.py`: Custom implementation and benchmark for Heap Sort.
  - `merge_sort.py`: Custom implementation and benchmark for Merge Sort.
  - `sort_numpy.py`: Benchmark using Python's NumPy.
  - `sort_c_plus_plus.cpp`: The C++ script to read the data and test `std::sort`.
- `Benchmark_Report.pdf`: My final report containing all the execution times, charts, and personal observations.
