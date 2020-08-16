#include <bits/stdc++.h>
using namespace std;

template <class T>
void Sort<T>::insertion_sort(vector<T> &input)
{
    for (int i = 1; i < input.size(); i++)
    {
        int k=i;
        int j = i - 1;
        while (j >= 0 && input[j] > input[k])
        {
            T temp = input[j];
            input[j] = input[k];
            input[k] = temp;
            j--;
            k--;
        }
    }
}
