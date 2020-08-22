#include<iostream>
#include<vector>
using namespace std;

int linearSearch(vector<int> arr, int key, int size) {
	for (int i = 0; i < size; i++) {
		cout << i << " ";
		if (arr[i] == key)
			return i;
	}
	return -1;

}
int main() {
	int n, key;
	 cin>> n;
	 vector<int> arr;
	//input 
	 for (int i = 0; i < n; i++) {
		 int input;
		 arr.push_back(input);
		 cin >> input;
	 }
	 int size = arr.size();
	 cin >> key;
	 int res = linearSearch(arr, key, size);
	 cout << "Found at position : " << res;

	return 0;
}
