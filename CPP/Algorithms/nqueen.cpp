#include <bits/stdc++.h>
using namespace std;
int isSafe(int n, int col, int row, vector<vector<int>> arr)
{
    if (row >= 0 && row < n && col < n && col >= 0)
    {
        if (arr[row][col] == 0)
        {
            for (int i = 0; i < n; i++)
            {
                if (arr[row][i] != 0)
                    return 2;
            }
            for (int i = 0; i < n; i++)
            {
                if (arr[i][col] != 0)
                    return 2;
            }
            for (int i = row, j = col; i < n && j < n; i++, j++)
            {
                if (arr[i][j] != 0)
                    return 2;
            }
            for (int i = row, j = col; i >= 0 && j >= 0; i--, j--)
            {
                if (arr[i][j] != 0)
                    return 2;
            }
            for (int i = row, j = col; i >= 0 && j < n; i--, j++)
            {
                if (arr[i][j] != 0)
                    return 2;
            }
            for (int i = row, j = col; i < n && j >= 0; i++, j--)
            {
                if (arr[i][j] != 0)
                    return 2;
            }
        }
        else
            return 2;
    }
    else
        return 0;
    return 1;
}

bool nqueen(int n, vector<vector<int>> &arr, int row)
{
    if (row == n)
        return true;
    for (int i = 0; i < n; i++)
    {
        bool res = isSafe(n, i, row, arr);
        if (res == 1)
        {
            arr[row][i] = 1;
            if (!nqueen(n, arr, row + 1))
                arr[row][i] = 0;
            else
                return true;
        }
        else if (res == 2)
            continue;
        else if (res == 0)
            return false;
    }
    return false;
}

int main()
{
    int n;
    cin >> n;
    vector<vector<int>> arr(n);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            arr[i].push_back(0);
    bool res = nqueen(n, arr, 0);
    // if (nqueen((int *)arr, 0, 0, n, 1))
    // {
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
            cout << " " << setw(2) << arr[i][j] << " ";
        cout << endl;
    }
    // }
    // else
    cout << "No solution possible";
    return 0;
}