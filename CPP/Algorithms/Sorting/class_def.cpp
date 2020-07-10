#include <bits/stdc++.h>
using namespace std;

template <class T>
class Sort
{
private:
    void merge_internal_1(vector<T> &, int, int, vector<T> &);
    void merge_internal_2(vector<T> &, int, int, int, vector<T> &);
    void radix_internal_1();
    void quick_internal_1(vector<T> &, int, int);
    void heap_internal(vector<T> &,int,int);
    int find_pivot(vector<T> &, int, int);

public:
    void bubble_sort(vector<T> &);
    void selection_sort(vector<T> &);
    void insertion_sort(vector<T> &);
    void merge_sort(vector<T> &);
    void quick_sort(vector<T> &);
    void counting_sort(vector<int> &, int);
    void radix_sort(vector<int> &);
    void heap_sort(vector<T> &);
    void display(vector<T>);
};

template <class T>
void Sort<T>::display(vector<T> input)
{
    for (int i = 0; i < input.size(); i++)
        cout << input[i] << " ";
}