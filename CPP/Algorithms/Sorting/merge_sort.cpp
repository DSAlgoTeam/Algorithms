#include <bits/stdc++.h>
using namespace std;

template <class T>
void Sort<T>::merge_internal_1(vector<T> &input, int low, int high, vector<T> &temp)
{
    if (low < high)
    {
        int mid = low + (high - low) / 2;
        merge_internal_1(input, low, mid, temp);
        merge_internal_1(input, mid + 1, high, temp);
        merge_internal_2(input, low, mid, high, temp);
    }
}

template <class T>
void Sort<T>::merge_internal_2(vector<T> &input, int low, int mid, int high, vector<T> &temp)
{
    int _low = low;
    int initial = low;
    int _mid = mid + 1;
    while (_low <= mid && _mid <= high)
    {
        if (input[_low] >= input[_mid])
        {
            temp[initial] = input[_mid];
            _mid++;
            initial++;
        }
        else
        {
            temp[initial] = input[_low];
            _low++;
            initial++;
        }
    }
    while (_low <= mid)
    {
        temp[initial] = input[_low];
        _low++;
        initial++;
    }
    while (_mid <= high)
    {
        temp[initial] = input[_mid];
        _mid++;
        initial++;
    }
    for (int i = low; i <= high; i++)
        input[i] = temp[i];
}

template <class T>
void Sort<T>::merge_sort(vector<T> &input)
{
    vector<T> temp(input.size());
    merge_internal_1(input, 0, input.size() - 1, temp);
}
