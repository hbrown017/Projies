/*
Name: Harry Brown III
Program: QuickSort
*/

#include <string>
#include <iostream>
#include <ctime>

using namespace std;


int partition(int *arr, int s, int e)
{
	srand(time(0));
	int pivot = arr[e];
	int pIndex = s;

	for (int i = s; i<e; i++)
	{
		if (arr[i] <= pivot)
		{
			swap(arr[i], arr[pIndex]);
			pIndex++;
		}
	}
	swap(arr[pIndex], arr[e]);
	return pIndex;
}
void quickSort(int *arr, int s, int e)
{
		if (s < e)
		{
			int pIndex = partition(arr, s, e);
			quickSort(arr, s, pIndex - 1);
			quickSort(arr, pIndex + 1, e);
		}
}

void display(int *arr, int n)
{
	for (int x = 1; x <= n; x++)
		cout << arr[x] << " ";
	cout << endl;
}

int main()
{
	int num = 0;
	int *arr;
	cout << "This program will generate random numbers to sort." << endl;
	cout << "How many numbers do you want to sort ? ";
	cin >> num;

	srand(time(0));
	arr = new int[num];

	cout << "A random list of values have been generated: ";
	for (int x = 0; x < num; x++)
	{
		arr[x] = rand() % 100;
		cout << arr[x] << " ";
	}

	//quick sort the values
	cout << endl;
	quickSort(arr, 0, num);

	cout << endl;
	//display the sorted values
	cout << "Sorted values: ";
	display(arr, num);

	return 0;
}