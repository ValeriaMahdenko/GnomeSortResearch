#pragma once
#include <iostream>

using namespace std;
void StupidSort(int *A, int n)
{
	int i = 0, tmp;
	while (i < n - 1)
	{
		if (A[i + 1] < A[i])
		{
			swap(A[i], A[i + 1]);
			i = 0;
		}
		else i++;
	}
}
