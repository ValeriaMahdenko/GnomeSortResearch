#pragma once
#include <iostream>
using namespace std;


void SelectionSort(int *data, int count)
{
	int min, temp; 
	for (int i = 0; i < count - 1; i++)
	{
		min = i;
		for (int j = i + 1; j < count; j++)  
		{
			if (data[j] < data[min])
				min = j;       
		}
		temp = data[i];      
		data[i] = data[min];
		data[min] = temp;
	}
}
