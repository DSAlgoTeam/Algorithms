#include <bits/stdc++.h>
using namespace std;

template <typename T>
struct Node
{
    T data;
    Node *next = NULL;
};

template <class T>
class LStack_LQueue
{
private:
    Node<T> *root = new Node<T>;
    Node<T> *head = root;

public:
    void stack_push(T);
    void stack_pop();
    void queue_push(T);
    void queue_pop();
};

template <class T>
void LStack_LQueue<T>::stack_push(T key)
{
    cout << "Pushed element is - " << key << endl;
    Node<T> *input = new Node<T>;
    input->data = key;
    head->next = input;
    head = input;
}

template <class T>
void LStack_LQueue<T>::stack_pop()
{
    if (root->next != NULL)
    {
        cout << "Popped element is - " << head->data << endl;
        Node<T> *temp = root;
        while (temp->next != head)
            temp = temp->next;
        head = temp;
        temp = temp->next;
        head->next = NULL;
        delete temp;
    }
    else
        cout << "Stack empty" << endl;
}

template <class T>
void LStack_LQueue<T>::queue_push(T key)
{
    cout << "Pushed element is - " << key << endl;
    Node<T> *input = new Node<T>;
    input->data = key;
    head->next = input;
    head = input;
}

template <class T>
void LStack_LQueue<T>::queue_pop()
{
    if (root->next != NULL)
    {
        cout << "Popped element is - " << root->next->data << endl;
        Node<T> *temp = root;
        root = root->next;
        delete temp;
    }
    else
        cout << "Queue is empty" << endl;
}