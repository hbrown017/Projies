/*
Name: Harry Brown III
Program: Linear and Binary Search
*/

#include <iostream>
#include <string>

using namespace std;

//linear search funtion
int linearSearch(int *arr, int s, int e, int key)
{
	if (s > e)
		return -1;
	else
	{
		if (arr[s] == key)
			return s;
		else
			return linearSearch(arr, s + 1, e, key);
	}
}

//binary search function
int binarySearch(int *arr, int s, int e, int key)
{
	if (s > e)
		return -1;
	else
	{
		int middle = (e + s) / 2;

		if (key > arr[middle])
			return binarySearch(arr, middle + 1, e, key);
		else if (key < arr[middle])
			return binarySearch(arr, s, middle + 1, key);
		else
			return middle;
	}
}

//display function
void display(int arr[], int e)
{
	cout << "Current values in the array: ";
	for (int x = 0; x < e; x++)
		cout << arr[x] << " ";
	cout << endl;
}

int main()
{
	int arrLin[] = {6,5,9,2,3,7,1,4,8};
	int arrBin[] = {2,3,7,9,12,15,17,20,24,26};
	int sizeLin = 8;
	int sizeBin = 9;
	int key = 0;
	int index = 0;

	cout << "Linear Search:" << endl;
	display(arrLin, sizeLin);

	cout << "Please enter one of the above values: ";
	cin >> key;
	index = linearSearch(arrLin, 0, sizeLin, key);
	cout << "Value " << key << " is found at index " << index << endl;

	cout << endl;
	cout << "Binary Search:" <<endl;
	display(arrBin, sizeBin);

	cout << "Please enter one of the above values: ";
	cin >> key;
	index = binarySearch(arrBin, 0, sizeBin, key);
	cout << "Value " << key << " is found at index " << index << endl;

	return 0;
}