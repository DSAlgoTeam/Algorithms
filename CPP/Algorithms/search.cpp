#include <bits/stdc++.h>
using namespace std;

template <class T>
class Search
{
private:
    vector<T> arr;
    T key;

public:
    Search(vector<T>, T);
    int LinearSearch(int);
    int BinarySearch(int, int);
};

template <class T>
Search<T>::Search(vector<T> arr, T key)
{
    this->arr = arr;
    this->key = key;
}

template <class T>
int Search<T>::LinearSearch(int size)
{
    for (int i = 0; i < size; i++)
    {
        if (arr[i] == key)
            return i + 1;
    }
    return -1;
}

template <class T>
int Search<T>::BinarySearch(int low, int high)
{
    if (low <= high)
    {
        int mid = low + (high - low) / 2;
        if (arr[mid] == key)
            return mid + 1;
        if (arr[mid] < key)
            return BinarySearch(mid + 1, high);
        else
            return BinarySearch(low, mid - 1);
    }
    return -1;
}