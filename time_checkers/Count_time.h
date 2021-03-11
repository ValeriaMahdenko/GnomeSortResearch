#pragma once
#include <ctime>
#include <iostream>
#include <chrono>

using namespace std;
auto check_time(int *arr, int count, void(*func)(int*, int))
{
	auto start = chrono::steady_clock::now();
	func(arr, count);
	auto finish = chrono::steady_clock::now();
	auto time = chrono::duration_cast<chrono::microseconds>(finish - start).count() / 1000.0;
	return time;
}
