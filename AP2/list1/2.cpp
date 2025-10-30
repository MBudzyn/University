#include <iostream>
using namespace std;

const long long MOD = 1000000000;

long long task2(long long a, long long n) {
    if (n == 0) return 1;
    long long x = task2(a, n / 2) % MOD;
    x = (x * x) % MOD;
    return (n % 2 == 0) ? x : (a * x) % MOD;
}

int main() {
    long long a, n;
    cin >> a >> n;
    cout << task2(a, n) << endl;
    return 0;
}