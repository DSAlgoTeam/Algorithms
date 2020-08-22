/*
This implementation of binary search will not entertain duplicate values in the input user
*/

#include<iostream>
#include<vector>
using namespace std;

int binarySearch(vector<int> arr, int l,int r, int key) {
	while (l <= r) {
		int mid = (l + (r - 1)) / 2;
		if (arr[mid] == key)
			return mid;
		else if (arr[mid] > key)
			r = mid - 1;
		else
			l = mid + 1;
	}
	return -1;
}
int main() {
	int n, key;
	cin >> n;
	vector<int> arr;
	//input 
	for (int i = 0; i < n; i++) {
		int input;
		arr.push_back(input);
		cin >> input;
	}
	int size = arr.size();
	cin >> key;
	int res = binarySearch(arr, 0, size-1, key);
	cout << "Found at position : " << res;

	return 0;
}
