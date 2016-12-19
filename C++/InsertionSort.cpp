/*
Name: Harry Brown III
Program: Insertion Sort
*/

#include <iostream>
#include <sstream>
#include <string>

using namespace std;

void insertionSort(int arr[], int n)
{
	//Insertion sort (Excellent 0(n) time)
	int temp = 0;
	int index = 0;
	cout << "Sorted values: ";
	for (int x = 0; x<n; x++)
	{
		for (int i = 1; i<n; i++)
		{
			temp = arr[i];
			index = i;
			while (index > 0 && arr[index - 1] > temp)
			{
				arr[index] = arr[index - 1]; //Swap higher value.
				index = index - 1; //Decrement index.
			}
			arr[index] = temp; //Swap lower value.
		}
		cout << arr[x] << " "; //Display value
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
	insertionSort(arr, arrSize);

	return 0;
}