#include <iostream>
using namespace std;

const long long MOD = 1000000007;

long long fastExponential(long long a, long long n) {
    if (n == 0) return 1;
    long long x = fastExponential(a, n / 2) % MOD;
    x = (x * x) % MOD;
    return (n % 2 == 0) ? x : (a * x) % MOD;
}

long long storeFactorial[1000001];
long long invFactorial[1000001];

int main() {
    storeFactorial[0] = 1;
    invFactorial[0] = 1;
    for (int i = 1; i <= 1000000; i++) {
        storeFactorial[i] = (storeFactorial[i - 1] * i) % MOD;
        invFactorial[i] = fastExponential(storeFactorial[i], MOD - 2);
    }

    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        int a, b;
        cin >> a >> b;
        cout << ((storeFactorial[a] * invFactorial[b]) % MOD * invFactorial[a - b]) % MOD << endl;
    }

    return 0;
}