#include <bits/stdc++.h>
using namespace std;

template <class T>
class Search
{
public:
    int LinearSearch(vector<T>, T, int);
    int BinarySearch(vector<T>, T, int, int);
};

template <class T>
int Search<T>::LinearSearch(vector<T> arr, T key, int size)
{
    for (int i = 0; i < size; i++)
    {
        if (arr[i] == key)
            return i + 1;
    }
    return -1;
}

template <class T>
int Search<T>::BinarySearch(vector<T> arr, T key, int low, int high)
{
    if (low <= high)
    {
        int mid = low + (high - low) / 2;
        if (arr[mid] == key)
            return mid + 1;
        if (arr[mid] < key)
            return BinarySearch(arr, key, mid + 1, high);
        else
            return BinarySearch(arr, key, low, mid - 1);
    }
    return -1;
}