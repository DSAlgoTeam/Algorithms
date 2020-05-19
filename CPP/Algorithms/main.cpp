#include <bits/stdc++.h>
#include "search.cpp"
using namespace std;
int main()
{
    while (1)
    {
        int a;
        int b;
        cout << "Select type of search:\n";
        cout << "1.Binary search\n2. Linear Search\n";
        cin >> b;
        cout << "Select datatype of operation:\n";
        cout << "1. Integer\n2. Float\n3. Char\n";
        cin >> a;
        int size;
        cout << "Enter size of array:\n";
        cin >> size;
        switch (a)
        {
        case 1:
        {
            vector<int> arr(size);
            int temp;
            for (int i = 0; i < size; i++)
                cin >> arr[i];
            int key;
            cout << "Enter key to be searched:\n";
            cin >> key;
            Search<int> search(arr, key);
            if (b == 1)
            {
                int result = search.BinarySearch(0, size - 1);
                if (result != -1)
                    cout << "Key found at-" << result << endl;
                else
                    cout << "Key not found\n";
            }
            else
            {
                int result = search.LinearSearch(size);
                if (result != -1)
                    cout << "Key found at:-" << result << endl;
                else
                    cout << "Key not found\n";
            }
        }
        case 2:
        {
            vector<float> arr(size);
            float temp;
            for (int i = 0; i < size; i++)
                cin >> arr[i];
            int key;
            cout << "Enter key to be searched:\n";
            cin >> key;
            Search<float> search(arr, key);
            if (b == 1)
            {
                int result = search.BinarySearch(0, size - 1);
                if (result != -1)
                    cout << "Key found at-" << result << endl;
                else
                    cout << "Key not found\n";
            }
            else
            {
                int result = search.LinearSearch(size);
                if (result != -1)
                    cout << "Key found at:-" << result << endl;
                else
                    cout << "Key not found\n";
            }
        }
        case 3:
        {
            vector<char> arr(size);
            char temp;
            for (int i = 0; i < size; i++)
                cin >> arr[i];
            int key;
            cout << "Enter key to be searched:\n";
            cin >> key;
            Search<char> search(arr, key);
            if (b == 1)
            {
                int result = search.BinarySearch(0, size - 1);
                if (result != -1)
                    cout << "Key found at-" << result << endl;
                else
                    cout << "Key not found\n";
            }
            else
            {
                int result = search.LinearSearch(size);
                if (result != -1)
                    cout << "Key found at:-" << result << endl;
                else
                    cout << "Key not found\n";
            }
        }
        break;
        }
    }
    return 0;
}