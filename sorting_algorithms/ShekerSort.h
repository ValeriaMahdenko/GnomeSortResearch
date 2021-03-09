#pragma once
#include <iostream>

using namespace std;
void ShekerSort(int *data, int count)
{
	int left = 0, right = count - 1; 
	int flag = 1;  
	while ((left < right) && flag > 0)
	{
		flag = 0;
		for (int i = left; i < right; i++) 
		{
			if (data[i] > data[i + 1]){
				swap(data[i], data[i + 1]);
				flag = 1;      
			}
		}
		right--; 
		for (int i = right; i > left; i--)  
		{
			if (data[i - 1] > data[i]) {
				swap(data[i], data[i - 1]);
				flag = 1;    
			}
		}
		left++; 
	}
}
