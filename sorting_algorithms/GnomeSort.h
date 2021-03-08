#pragma once
#include <iostream>
#include <fstream>
using namespace std;

auto GnomeSort(int* data, int count) {
//    for (int i = 1; i < count; ) {
//        if (data[i - 1] <= data[i])
//            ++i;
//        else {
//            int tmp = data[i];
//            data[i] = data[i - 1];
//            data[i - 1] = tmp;
//            --i;
//            if (i == 0)
//                i = 1;
//        }
//    }

    int index = 0;

    while (index < count) {
        if (data[index] >= data[index - 1] || index == 0)
            index++;
        else {
            swap(data[index], data[index - 1]);
            index--;
        }
    }

}
