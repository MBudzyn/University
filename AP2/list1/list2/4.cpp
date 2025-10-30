#include <iostream>
#include <vector>
using namespace std;

vector<int> sieveEra(int n) {
    vector<int> sieve(n + 1, 1);
    vector<bool> visited(n + 1, false);

    for (int i = 1; i<= n ; i++) {
        sieve[i] = i;
    }

    for (int i = 2; i <= n; i++) {
        if (!visited[i]) {
            sieve[i] = i-1;
            for (int j = i*2; j <= n; j += i) {
                visited[j] = true;
                sieve[j] *= (1 - 1 / (double) i);
            }
        }
    }
    return sieve;
}


int main() {
    vector<int> sieve1 = sieveEra(1000000);
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        cout << sieve1[x] << endl;
    }

    return 0;
}