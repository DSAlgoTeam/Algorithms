#include <bits/stdc++.h>
using namespace std;

template <typename T>
struct Node
{
    T data;
    Node *left = NULL;
    Node *right = NULL;
};

template <class T>
class Tree
{
private:
    Node<T> *root = new Node<T>;
    int mark = 1;

public:
    Node<T> *constructTree(vector<T>, Node<T> *, int, int); //returns root Node
    Node<T> *getNode();
    void inorder(struct Node<T> *);
    void preorder(struct Node<T> *);
    void postorder(struct Node<T> *);
    void addNode(T);
};

template <class T>
Node<T> *Tree<T>::constructTree(vector<T> arr, Node<T> *root, int i, int n)
{
    if (i < n)
    {
        Node<T> *temp = new Node<T>;
        temp->data = arr[i];
        root = temp;
        root->left = constructTree(arr, root->left, 2 * i + 1, n);
        root->right = constructTree(arr, root->right, 2 * i + 2, n);
    }
    return root;
}

template <class T>
Node<T> *Tree<T>::getNode()
{
    return root;
}

template <class T>
void Tree<T>::inorder(struct Node<T> *root)
{
    inorder(root->left);
    cout << root->data << " ";
    inorder(root->right);
}

template <class T>
void Tree<T>::preorder(struct Node<T> *root)
{
    cout << root->data << " ";
    inorder(root->left);
    inorder(root->right);
}

template <class T>
void Tree<T>::postorder(struct Node<T> *root)
{
    inorder(root->left);
    inorder(root->right);
    cout << root->data << " ";
}

template <class T>
void Tree<T>::addNode(T data)
{
    if (mark)
    {
        root->data = data;
        mark = 0;
    }
    else
    {
        Node<T> *temp = root;
        while (1)
        {
            if (data >= temp->data)
            {
                if (temp->right == NULL)
                {
                    Node<T> *input = new Node<T>;
                    input->data = data;
                    temp->right = input;
                    break;
                }
                else
                    temp = temp->right;
            }
            else
            {
                if (temp->left == NULL)
                {
                    Node<T> *input = new Node<T>;
                    input->data = data;
                    temp->left = input;
                    break;
                }
                else
                    temp = temp->left;
            }
        }
    }
}