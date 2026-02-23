#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <chrono>
#include <string>

using namespace std;

void process_and_sort(const string& filename) {
    ifstream file(filename);
    if (!file) return; 

    vector<double> data;
    double value;
    while (file >> value) {
        data.push_back(value);
    }
    
    auto start = chrono::high_resolution_clock::now();
    sort(data.begin(), data.end());
    auto stop = chrono::high_resolution_clock::now();
    
    chrono::duration<double, milli> ms = stop - start;
    
    cout << filename << ": " << ms.count() << " ms\n";
}

int main() {
    string files[] = {
        "data/test_0_float.txt", "data/test_1_float.txt", "data/test_2_float.txt",
        "data/test_3_float.txt", "data/test_4_float.txt", "data/test_5_int.txt",
        "data/test_6_int.txt", "data/test_7_int.txt", "data/test_8_int.txt",
        "data/test_9_int.txt"
    };

    for (const auto& f : files) {
        process_and_sort(f);
    }

    return 0;
}
