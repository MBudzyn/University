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
long long invFactorial[1000001];#include <iostream>
#include <vector>
using namespace std;

class Task {
public:
    int N;
    vector<int> input_data;
    vector<int> pom_table;
    int two_power;

    Task() {
        run();
    }

    int min_to_power(int n) {
        int i = 1;
        while (i < n) i *= 2;
        return i;
    }

    void run() {
        loadData();
        solve();
    }

    void fill_default() {
        for (int i = 0; i < N; i++) {
            pom_table[two_power + i] = 1;
        }
        for (int i = two_power - 1; i > 0; i--) {
            pom_table[i] = pom_table[left_child(i)] + pom_table[right_child(i)];
        }
    }

    int left_child(int index) {
        return index * 2;
    }

    int right_child(int index) {
        return index * 2 + 1;
    }

    int parent(int index) {
        return index / 2;
    }

    void update(int index) {
        int par = two_power + index;
        pom_table[par] = 0;
        while (par > 1) {
            par = parent(par);
            int left = left_child(par);
            int right = right_child(par);
            pom_table[par] = pom_table[left] + pom_table[right];
        }
    }
    int answer(int p) {
        int index = 1;
        while (index < two_power) {
            int left = left_child(index);
            int right = right_child(index);

            if (pom_table[left] >= p) {
                index = left;
            } else {
                p -= pom_table[left];
                index = right;
            }
        }
        return index - two_power;
    }

    void solve() {
        for (int i = 0; i < N; i++) {
            int p;
            cin >> p;
            int idx = answer(p);
            cout << input_data[idx] << " ";
            update(idx);
        }
        cout << endl;
    }

    void loadData() {
        cin >> N;
        two_power = min_to_power(N);
        pom_table.resize(2 * two_power);
        input_data.resize(N);
        for (int i = 0; i < N; i++) {
            cin >> input_data[i];
        }
        fill_default();
    }
};

int main() {
    Task t;
    return 0;
}


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