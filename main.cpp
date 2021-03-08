#include <iostream>
#include <fstream>
#include <algorithm>
#include "GnomeSort.h"
#include "Count_time.h"
#include <chrono>

using namespace std;


void printArray(int arr[], int n)
{
    cout << "Sorted sequence after Gnome sort: ";
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
    cout << "\n";
}

void rand_arr(int *arr, int count)
{
    for (int i = 0; i < count; i++)
        arr[i] = 1 + rand() % 1000;
}

void create_csv_for_one(const string &file_name, int min_c, int max_c, int step){
    ofstream outputFile;
    outputFile.open(file_name, std::ios::out | std::ios::app);

    for (int i = min_c; i < max_c; i += step)
        outputFile << i << ",";
    outputFile << max_c << "\n";
}


void create_csv(const string &file_name, int min_c, int max_c, int step){
    ofstream outputFile;
    outputFile.open(file_name, std::ios::out | std::ios::app);
    outputFile << "Algorithm";
    for (int i = min_c; i <= max_c; i += step) {
        outputFile << "," << i;
    }
    outputFile << "\n";
    outputFile.close();
}

void test_algorithm(const string &file_name, int min_c, int max_c, int step, void(*func)(int*, int), int sort_p=0){

    ofstream outputFile;
    outputFile.open(file_name, std::ios::out | std::ios::app);

    for (int i = min_c; i < max_c; i += step)
    {
        int *arr = new int[i];
        rand_arr(arr, i);
        if (sort_p > 0) sort(arr, arr + i);
        else if (sort_p < 0) sort(arr, arr + i, [](const int a, const int b) {return a > b; });

        auto time_random = check_time(arr, i, func);
        outputFile << time_random << ",";
    }
    int *arr = new int[max_c];
    rand_arr(arr, max_c);
    if (sort_p > 0) sort(arr, arr + max_c);
    else if (sort_p < 0) sort(arr, arr + max_c, [](const int a, const int b) {return a > b; });

    auto time_random = check_time(arr, max_c, func);
    outputFile << time_random << "\n";
    outputFile.close();
}

int main()
{
    string file = "/Users/sophiyca/CLionProjects/GnomeResearch/Gnome_sorted.csv";
    int min = 500, max = 100000, step = 500;

    create_csv_for_one(file, min, max, step);
    test_algorithm(file, min, max, step, GnomeSort, 1);

    
    system("pause");
    return 0;
}
