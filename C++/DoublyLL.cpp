/*
Name: Harry Brown III
Program: Doubly linked list
Description:
	This program implements a doubly linked list through the use of a "Link" class and nested "node" class.
	The program prompts the user to input values to the list and then displays a menu of options for the
	user to choose from. Options include: deleting first node, deleting last node, adding node to the front
	or adding node to the back.
*/

#include <iostream>
#include <sstream>
#include <string>

using namespace std;

class Link
{
private:
	class node
	{
	public:
		int data;
		node * next;
		node * prev;

		node(int x)
		{data = x;}
	};

	node * head;
	node * tail;
	friend void menu(Link list);

public:
	Link()
	{
		head = NULL;
		tail = NULL;
	}

	void insert(int x)
	{
		node * NODE = new node(x);
		if (head == NULL)
		{
			NODE->prev = NULL;
			head = NODE;
			tail = NODE;
			NODE->next = NULL;
		}
		else
		{
			tail->next = NODE;
			NODE->prev = tail;
			tail = NODE;
			tail->next = NULL;
		}
	}

	void addBack(int x)
	{
		node * NODE = new node(x);
		tail->next = NODE;
		NODE->prev = tail;
		tail = NODE;
		tail->next = NULL;
	}

	void addFront(int x)
	{
		node * NODE = new node(x);
		NODE->prev = NULL;
		head->prev = NODE;
		NODE->next = head;
		head = NODE;
	}

	int removeFront()
	{
		int output = head->data;
		node * doom = head;

		if (head == tail) //when only one node left in list
			head, tail = NULL;
		else
		{
			head = head->next;
			head->prev = NULL; //so previous won't point to trash
		}
		delete doom;
	
		return output;
	}

	int removeBack()
	{
		int output = tail->data;
		node *doom = tail;

		if (head == tail) //when only one node left in list
			head, tail = NULL;
		else
		{
			tail = tail->prev;
			tail->next = NULL; //so next won't point to trash
		}
		delete doom;

		return output;
	}

	void display()
	{
		//change current to tail and current->next to current->prev to flip value output
		node * current = head;

		while (current != NULL)
		{
			cout << current->data << endl;
			current = current->next;
		}
	}

};


int* getInput(int &arrSize)
{
	Link list; //create list object

	//prompt client for input
	cout << "How many values do you want to insert into the doubly linked list? ";
	cin >> arrSize;

	//create a dynamic array of integers
	int *arr;
	arr = new int[arrSize];
	string values;

	//set client values
	cout << "Please enter " << arrSize << " values (seperated by space) to insert to the doubly linked list: ";
	cin.ignore();
	getline(cin, values);

	//parse string values into an array
	stringstream sStream(values);
	for (int x = 0; x < arrSize; x++)
		sStream >> arr[x];

	return arr;
}

void menu(Link list)
{
	bool go = true;
	int choice = 0;
	int addVal = 0;

	while (go)
	{
		cout << endl;
		cout << "Select an option:" << endl;
		cout << "1. Delete value from the front of the list." << endl;
		cout << "2. Delete value from the back of the list." << endl;
		cout << "3. Add value to the front of the list." << endl;
		cout << "4. Add value to the back of the list." << endl;
		cout << "5. Exit" << endl;
		cout << "Option: ";
		cin >> choice;

		switch (choice) {
		case 1:
			list.removeFront();
			break;
		case 2:
			list.removeBack();
			break;
		case 3:
			cout << endl;
			cout << "Enter a value to add to the front: ";
			cin >> addVal;
			list.addFront(addVal);
			break;
		case 4:
			cout << endl;
			cout << "Enter a value to add to the back: ";
			cin >> addVal;
			list.addBack(addVal);
			break;
		case 5:
			go = false;
			break;
		default:
			cout << "Please enter 1, 2, 3, or 4." << endl;
		}

		//display changes made to linked list
		cout << endl;
		if (list.head != NULL && list.tail != NULL)
		{
			cout << "Modified linked list: " << endl;
			list.display();
		}
		else
		{
			cout << "The list is empty. The program will now exit." << endl;
			go = false;
		}
	}
}


int main()
{
	Link list;
	int arrSize = 0;
	int *arr;

	arr = getInput(arrSize); //get user input and store values in array
	
	//insert array values into linked list
	for (int x = 0; x < arrSize; x++)
		list.insert(arr[x]);

	cout << "Generated linked list: " << endl;
	list.display(); //display values in the list

	//call menu function
	menu(list);

	return 0;
}