#pragma once
#include <iostream>
using namespace std;

void BubleSort(int* data, int count) {
	auto temp = 0;
	for (int i = 0; i < count - 1; i++) {
		for (int j = 0; j < count - i - 1; j++) {
			if (data[j] > data[j + 1]) {
				temp = data[j];
				data[j] = data[j + 1];
				data[j + 1] = temp;
			}
		}
	}
}
