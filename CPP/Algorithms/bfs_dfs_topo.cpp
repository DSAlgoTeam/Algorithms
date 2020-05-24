#include <bits/stdc++.h>
using namespace std;

template <class T>
class Graph
{
private:
    map<T, vector<T>> storage;
    map<T, int> mark;

public:
    void breadth_first_search(T);
    void depth_first_search(T);
    void topo_sort();
    void addNode(T, T);
};

template <class T>
void Graph<T>::addNode(T a, T b)
{
    storage[a].push_back(b);
    mark[a] = 0;
    mark[b] = 0;
}

template <class T>
void Graph<T>::depth_first_search(T start)
{
    auto i = storage.begin();
    for (; i != storage.end(); i++)
    {
        if (i->first == start)
            break;
    }
    int count = 0;
    while (count != storage.size())
    {
        if (i == storage.end())
            i = storage.begin();
        cout << i->first << " ";
        count++;
        mark[i->first] = 1;
        i++;
    }
    i--;
    while (count)
    {
        if (i == storage.begin())
        {
            i = storage.end();
            i--;
        }
        for (auto k = i->second.begin(); k != i->second.end(); k++)
        {
            if (mark[*k] == 0)
            {
                cout << *k << " ";
                mark[*k] = 1;
            }
        }
        i--;
        count--;
    }
}

template <class T>
void Graph<T>::breadth_first_search(T start)
{
    auto i = storage.begin();
    for (; i != storage.end(); i++)
    {
        if (i->first == start)
            break;
    }
    int count = 0;
    while (count != storage.size())
    {
        if (i == storage.end())
            i = storage.begin();
        if (mark[i->first] != 1)
        {
            cout << i->first << " ";
            mark[i->first] = 1;
        }
        for (auto k = i->second.begin(); k != i->second.end(); k++)
        {
            if (mark[*k] != 1)
            {
                cout << *k << " ";
                mark[*k] = 1;
            }
        }
        count++;
        i++;
    }
}

template <class T>
void Graph<T>::topo_sort()
{
    stack<T> Stack;
    int count = 0;
    auto i = storage.begin();
    while (count != storage.size())
    {
        if (mark[i->first] != 1)
        {
            Stack.push(i->first);
            mark[i->first] = 1;
        }
        for (auto k = i->second.begin(); k != i->second.end(); k++)
        {
            if (mark[*k] != 1)
            {
                Stack.push(*k);
                mark[*k] = 1;
            }
        }
        count++;
        i++;
    }
    while (Stack.empty() == false)
    {
        cout << Stack.top() << " ";
        Stack.pop();
    }
}