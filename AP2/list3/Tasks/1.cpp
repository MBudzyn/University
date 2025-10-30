#include <iostream>
#include <vector>

using namespace std;

long long fastExponential(long long a, long long n, long long mod) {
    if (n == 0) return 1;
    long long x = fastExponential(a, n / 2, mod) % mod;
    x = (x * x) % mod;
    return (n % 2 == 0) ? x : (a * x) % mod;
}

vector<vector<int>> loadData(int k) {
    vector<int> p(k);
    vector<int> a(k);
    for (int i = 0; i < k; i++) {
        cin >> p[i] >> a[i];
    }
    return {p, a};
}

long long CRT(const vector<int>& p, const vector<int>& a) {
    long long res = 0, M = 1;
    for (int i : p) {
        M *= i;
    }
    for (int i = 0; i < p.size(); i++) {
        long long Mi = M / p[i];
        long long inv = fastExponential(Mi, p[i] - 2, p[i]);
        res += ((((a[i] % M) * (Mi % M)) % M) * (inv % M)) % M;
    }
    return res % M;
}

int main() {
    int N, K;
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> K;
        vector<vector<int>> data = loadData(K);
        cout << CRT(data[0], data[1]) << endl;
    }
    return 0;
}