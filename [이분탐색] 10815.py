#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void binarySearch(vector<int>& arr, int lt, int rt, int ans) {
    if (lt > rt) {
        cout << "0 ";
        return;
    }
    else{
        int m = (lt + rt) / 2;
        if (arr[m] == ans) {
            cout << "1 ";
            return;
        }
        else if (arr[m] > ans)
            return binarySearch(arr, lt, m-1, ans);
        else
            return binarySearch(arr,m+1, rt, ans);
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int num1;
    cin >> num1;
    vector<int> arr;
    for (int i = 0; i < num1; ++i) {
        int cur;
        cin >> cur;
        arr.push_back(cur);
    }
    sort(arr.begin(), arr.end());

    int num2;
    cin >> num2;
    for (int i = 0; i < num2; ++i) {
        int cur;
        cin >> cur;
        binarySearch(arr,0,num1-1, cur);
    }
}


