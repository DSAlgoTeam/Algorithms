#include <bits/stdc++.h>
using namespace std;

template <class T>
void Sort<T>::selection_sort(vector<T> &input)
{
    for (int i = 0; i < input.size() - 1; i++)
    {
        T min = i;
        for (int j = i + 1; j < input.size(); j++)
        {
            if (input[min] > input[j])
                min = j;
        }
        T temp = input[i];
        input[i] = input[min];
        input[min] = temp;
    }
}
