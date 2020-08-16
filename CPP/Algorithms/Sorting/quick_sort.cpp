#include<bits/stdc++.h>
using namespace std;

template<class T>
void Sort<T>::quick_internal_1(vector<T> &input,int low,int high)
{
    if(low<high)
    {
        int pivot=find_pivot(input,low,high);
        quick_internal_1(input,low,pivot-1);
        quick_internal_1(input,pivot+1,high);
    }
}

template<class T>
int Sort<T>::find_pivot(vector<T> &input,int low,int high)
{
    int pivot=low;
    while(low<high)
    {
        while(input[pivot]>input[low])
            low++;
        while(input[high]>input[pivot])
            high--;
        T temp=input[low];
        input[low]=input[high];
        input[high]=temp;
    }
    T temp=input[pivot];
    input[pivot]=input[high];
    input[high]=temp;
    return high;
}

template<class T>
void Sort<T>::quick_sort(vector<T> &input)
{
    quick_internal_1(input,0,input.size()-1);
}