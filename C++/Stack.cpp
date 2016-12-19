/*
Name: Harry Brown III
Program: Stack class
*/

#include <iostream>
#include <sstream>
#include <string>

using namespace std;

class stack
{
private:
	int index;
	int size;
	int *arr;
public:
	stack()
	{
		index = 0;
		size = 10;
		arr = new int[size];
	}

	stack(int s) //parameterized constructor
	{
		index = 0;
		size = s;
		arr = new int[size];
	}

	void push(int x) //push function
	{arr[index++] = x;}

	int pop() //pop function
	{return arr[--index];}

	void display() //display function
	{
		for (int i = index-1; i>=0; i--)
			cout << arr[i] << endl;
	}
};

int main()
{
	int numPop = 0;
	int arrSize = 0;

	//prompt client input
	cout << "How many values do you want to push on the stack? ";
	cin >> arrSize;

	stack s(arrSize); //create stack class object

	//create a dynamic array of integers
	int *arr;
	arr = new int[arrSize];
	string values;

	//set client values
	cout << "Please enter " << arrSize << " values (seperated by space) to push on the stack: ";
	cin.ignore();
	getline(cin, values);

	//parse string values
	stringstream sStream(values);
	for (int x = 0; x < arrSize; x++)
	{
		sStream >> arr[x];
		s.push(arr[x]); //push client values on to the stack
	}

	cout << "Items in the stack: " << endl;
	s.display(); //display stack values

	cout << endl;
	cout << "How many values do you want to pop off the stack? ";
	cin >> numPop;

	cout << "Items removed from stack: ";
	for (int x = 0; x < numPop; x++)
		cout << s.pop() << " "; //pop client values off the stack
	cout << endl;

	cout << endl;
	cout << "Items remaining in stack: " << endl;
	s.display(); //display remaining values in stack

	return 0;
}