#include <bits/stdc++.h>
using namespace std;

template <class T>
class Stack
{
private:
    vector<T> arr;

public:
    void push(T);
    void pop();
};

template <class T>
void Stack<T>::push(T key)
{
    cout << "Pushed element - " << key << endl;
    arr.push_back(key);
}

template <class T>
void Stack<T>::pop()
{
    if (arr.size() > 0)
    {
        cout << "Popped element is - " << arr[arr.size() - 1] << endl;
        arr.pop_back();
    }
    else
        cout << "Stack empty\n";
}



template <class T>
class Queue
{
private:
    vector<T> arr;

public:
    void push(T);
    void pop();
};

template <class T>
void Queue<T>::push(T key)
{
    cout << "Pushed element - " << key << endl;
    arr.push_back(key);
}

template <class T>
void Queue<T>::pop()
{
    if (arr.size() > 0)
    {
        cout << "Popped element is - " << arr[0] << endl;
        auto i = arr.begin();
        arr.erase(i);
    }
    else
        cout << "Queue empty\n";
}