#include <bits/stdc++.h>
using namespace std;

template <class T>
void Sort<T>::bubble_sort(vector<T> &input)
{
    for(int i=0;i<input.size()-1;i++)
    {
        for(int j=i+1;j<input.size();j++)
        {
            if(input[i]>input[j])
            {
                T temp=input[i];
                input[i]=input[j];
                input[j]=temp;
            }
        }
    }
}
