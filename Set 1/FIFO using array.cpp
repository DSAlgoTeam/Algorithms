/*
FIFO Data Structure - Array 
Circular Queue implementation using class
*/

#include<iostream>
using namespace std;
template<class X>
class circularQueue {
	int rear, front;
	int size;
	X* arr;
	circularQueue(X n) {
		front = rear = -1;
		size = n;
		arr = new X[n];
	}
	void enQueue(X data) {
		//assume that rear is pointing at index 1 and front is pointing at index 2 for the second condition
		if ((front == 0 && rear == size - 1) || (rear == (front - 1) % (size - 1))) {
			cout<<"Queue overflow";
			return;
		}
		//empty queue
		else if (front == -1) {
			front = rear = 0;
				arr[rear] = data;
		}
		//not empty queue but a few spaces are left before the front pointer
		else if (front != 0 && rear == size - 1) {
			rear = 0;
				arr[rear] = data;
		}
		//from the front of the queue the array is full but a few spaces are left after the rear pointer
		else {
			rear++;
			arr[rear] = data;
		}
	}
	X deQueue() {
		if (front == -1) {
			cout << "Empty queue";
			return -1;
		}
		int data = arr[front];
		arr[front] = -1;
		//after deleting all the elements front has reached rear, so now after dequeuing the last element, I need to initialize 
		//both front and rear with -1
		if (front == rear) {
			front = -1;
			rear = -1;
		}
		//front has reached at the end of queue. Now to delete the data at the front of the queue, front should be made to 0
		else if (front == size - 1)
			front = 0;
		//the normal case where after deleting the data, we increment the front
		else
			front++;
		return data;
	}
	void display() {
		if (front == -1) {
			cout << "Empty queue";
			return;
		}
		cout << endl<<"Elements in queue are : ";
		if (rear >= front) {
			for (int i = 0; i <= rear; i++)
				cout << arr[i]<<" ";
		}
		//for case when rear is smaller than front with respect to index values
		else {
			for (int i = front; i < size; i++)
				cout << arr[i]<<" ";
			for (int i = 0; i <= rear; i++)
				cout << arr[i]<<" ";
		}
		cout << endl;
	}
};
