#pragma once
#include <iostream>
using namespace std;

void InsertSort(int* data, int count) {
	int  x;
	long i, j;

	for (i = 0; i < count; i++) { 
		x = data[i];
		for (j = i - 1; j >= 0 && data[j] > x; j--)
			data[j + 1] = data[j];  	
		data[j + 1] = x;
	}
}
