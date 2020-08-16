#include <bits/stdc++.h>
using namespace std;
class Hashing
{
private:
    vector<int> arr;
    int prime;
    int hash2(int);
    void calculatePrime(int);
    int checkPrime(int);

public:
    void insert(vector<int>);
    vector<int> LinearProbing();
    vector<int> QuadraticProbing();
    vector<int> DoubleHashing();
};

int Hashing::hash2(int key)
{
    return (prime - (key % prime));
}

void Hashing::insert(vector<int> arr)
{
    this->arr = arr;
}

void Hashing::calculatePrime(int n)
{
    for (int i = n - 1; i > 0; i--)
    {
        int p = checkPrime(i);
        if (p)
        {
            this->prime = p;
            return;
        }
    }
    this->prime = 1;
}

int Hashing::checkPrime(int n)
{
    for (int i = 2; i <= sqrt(n); i++)
    {
        if (n % i == 0)
            return 0;
    }
    return 1;
}

vector<int> Hashing::LinearProbing()
{
    vector<int> hashTable(arr.size());
    for (int i = 0; i < arr.size(); i++)
    {
        int n = arr[i] % arr.size();
        int count = 0;
        while (hashTable[n] != 0)
            n = (arr[i] + count++) % arr.size();
        hashTable[n] = arr[i];
    }
    return hashTable;
}

vector<int> Hashing::QuadraticProbing()
{
    calculatePrime(arr.size());
    vector<int> hashTable(arr.size());
    for (int i = 0; i < arr.size(); i++)
    {
        int n = arr[i] % arr.size();
        int count = 0;
        while (hashTable[n] != 0)
            n = (arr[i] + (count++) ^ 2) % arr.size();
        hashTable[n] = arr[i];
    }
    return hashTable;
}

vector<int> Hashing::DoubleHashing()
{
    vector<int> hashTable(arr.size());
    for (int i = 0; i < arr.size(); i++)
    {
        int n = arr[i] % arr.size();
        int count = 0;
        while (hashTable[n] != 0)
            n = (arr[i] + (count++) * hash2(arr[i])) % arr.size();
    }
    return hashTable;
}