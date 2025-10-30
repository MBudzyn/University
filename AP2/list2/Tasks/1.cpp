#include <iostream>
#include <vector>

using namespace std;

vector<int> GCD(int a, int b) {
    if (b == 0) return {1, 0, a};
    vector<int> res = GCD(b, a % b);
    int k = res[0], l = res[1], d = res[2];
    return {l,  k - (a / b) * l, d};
}

int main() {
    int n;
    cin >> n;
    int a, b;
    for (int i = 0; i < n; i++) {
        cin >> a >> b;
        vector<int> res = GCD(a, b);
        cout << res[0] << " " << res[1] << " " << res[2] << endl;
    }

    return 0;
}


