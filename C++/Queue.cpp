/*
Name: Harry Brown III
Program: Queue class
*/

#include <iostream>
#include <sstream>
#include <string>

using namespace std;

class Queue
{
private:
	int head;
	int tail;
	int size;
	int *arr;

public:
	Queue()
	{
		head = 0;
		tail = 0;
		size = 10;
		arr = new int[size];
	}

	Queue(int s)
	{
		head = 0;
		tail = 0;
		size = s;
		arr = new int[size];
	}

	void enqueue(int x)
	{arr[tail++] = x;} //puts tail at last value index
	
	int dequeue()
	{return arr[head++];} 

	void display()
	{
		for (int i = tail-1; i>=head; i--)
			cout << arr[i] << endl;
	}
};

int main()
{
	
	int numPop = 0;
	int arrSize = 0;

	//prompt client input
	cout << "How many values do you want to insert into the queue? ";
	cin >> arrSize;

	Queue q(arrSize); //create stack class object

	//create a dynamic array of integers
	int *arr;
	arr = new int[arrSize];
	string values;

	//set client values
	cout << "Please enter " << arrSize << " values (seperated by space) to insert to the queue: ";
	cin.ignore();
	getline(cin, values);

	//parse string values
	stringstream sStream(values);
	for (int x = 0; x < arrSize; x++)
	{
		sStream >> arr[x];
		q.enqueue(arr[x]); //push client values on to the stack
	}

	cout << "Items in the stack: " << endl;
	q.display(); //display stack values

	cout << endl;
	cout << "How many values do you want to remove from the queue? ";
	cin >> numPop;

	cout << "Items removed from the queue: ";
	for (int x = 0; x < numPop; x++)
		cout << q.dequeue() << " "; //pop client values off the stack
	cout << endl;

	cout << endl;
	cout << "Items remaining in queue: " << endl;
	q.display(); //display remaining values in stack
	
	return 0;
}