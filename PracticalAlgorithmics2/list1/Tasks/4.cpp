#include <iostream>
#include <vector>
using namespace std;

int binarySearch(vector<int>& arr, int x) {
    int left = 0, right = arr.size() - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] == x)
            return mid + 1;
        else if (arr[mid] < x)
            left = mid + 1;
        else
            right = mid - 1;
    }
    return -1;
}

int main() {
    int N;
    cin >> N;
    vector<int> arr(N);
    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }

    int M;
    cin >> M;
    while (M--) {
        int x;
        cin >> x;
        cout << binarySearch(arr, x) << '\n';
    }

    return 0;
}
