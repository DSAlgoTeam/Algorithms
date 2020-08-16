#include <bits/stdc++.h>
using namespace std;

template <class T>
void Sort<T>::heap_internal(vector<T> &input, int n, int i)
{
    int largest = i;
    int l = 2 * i + 1;
    int r = 2 * i + 2;
    if (l < n && input[l] > input[largest])
        largest = l;
    if (r < n && input[r] > input[largest])
        largest = r;
    if (largest != i)
    {
        swap(input[i], input[largest]);
        heap_internal(input, n, largest);
    }
}

template <class T>
void Sort<T>::heap_sort(vector<T> &input)
{
    int n = input.size();
    for (int i = n / 2 - 1; i >= 0; i--)
        heap_internal(input, n, i);
    for (int i = n - 1; i > 0; i--)
    {
        swap(input[0], input[i]);
        heap_internal(input, i, 0);
    }
}