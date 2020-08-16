#include<bits/stdc++.h>
#include "counting_sort.cpp"
using namespace std;

template<class T>
void Sort<T>::radix_internal_1(vector<int> &input)
{
    
}

template<class T>
void Sort<T>::radix_sort(vector<int> &input)
{
    int max=max_element(input.begin(),input.end());
    int count=0;
    while(max)
    {
        count++;
        max=max/10;
    }
    for(int i=0;)
}