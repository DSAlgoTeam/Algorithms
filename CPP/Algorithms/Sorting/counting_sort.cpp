#include <bits/stdc++.h>
using namespace std;

template <class T>
void Sort<T>::counting_sort(vector<int> &input, int k)
{
    vector<int> count(k + 1);
    for (int i = 0; i <= k; i++)
        count[i] = 0;
    for (int i = 0; i < input.size(); i++)
        count[input[i]]++;

    for (int i = 1; i <= k; i++)
        count[i] = count[i] + count[i - 1];

    vector<int> result(input.size());
    for (int i = 0; i < input.size(); i++)
    {
        int n = count[input[i]] - count[input[i] - 1];
        int temp = count[input[i]] - 1;
        while (n-- > 0 && result[temp] == 0)
            result[temp--] = input[i];
    }
    input = result;
}