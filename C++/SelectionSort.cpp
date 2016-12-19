/*
Name: Harry Brown III
Program: Selection Sort
*/

#include <iostream>
#include <sstream>
#include <string>

using namespace std;

void selectionSort(int arr[], int n)
{
	cout << "Sorted values: ";
	for (int x = 0; x < n; x++)
	{
		int minIndex = x;
		for (int y = x; y < n; y++)
		{
			if (arr[minIndex] > arr[y])
				minIndex = y;
		}

		int temp = arr[x];
		arr[x] = arr[minIndex];
		arr[minIndex] = temp;

		cout << arr[x] << " ";
	}
	cout << endl;
}

int main()
{
	int arrSize = 0;
	cout << "How many values do you need to sort? ";
	cin >> arrSize;

	//create a dynamic array of integers.
	int *arr;
	arr = new int[arrSize];
	string values;

	//set values
	cout << "Please enter " << arrSize << " values (seperated by space) to sort: ";
	cin.ignore();
	getline(cin, values);

	//parse string values
	stringstream sStream(values);
	for (int x = 0; x < arrSize; x++)
		sStream >> arr[x];

	//call sorting fuction
	selectionSort(arr, arrSize);

	return 0;
}