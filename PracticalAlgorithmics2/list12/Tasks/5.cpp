#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Task {
private:
    const int B1 = 931;
    const int MOD1 = 1e9 + 7;
    const int B2 = 937;
    const int MOD2 = 1e9 + 9;

    string T, P;
    vector<int> power1, prefixHash1;
    vector<int> power2, prefixHash2;

    int result = 0;

    int mod(int x, int MOD) {
        return (x % MOD + MOD) % MOD;
    }

    int charToInt(char c) {
        return c - 'a' + 1;
    }

    int getHash(const vector<int>& prefixHash, const vector<int>& power, int l, int r, int MOD) {
        int hashVal = prefixHash[r + 1] - 1LL * prefixHash[l] * power[r - l + 1] % MOD;
        return mod(hashVal, MOD);
    }

    int computeHash(const string& s, int base, int MOD) {
        int h = 0;
        for (char c : s) {
            h = (1LL * h * base + charToInt(c)) % MOD;
        }
        return h;
    }

    void prepareHashing() {
        int n = T.size();
        power1.resize(n + 1);
        prefixHash1.resize(n + 1);
        power2.resize(n + 1);
        prefixHash2.resize(n + 1);

        power1[0] = power2[0] = 1;
        for (int i = 1; i <= n; ++i) {
            power1[i] = 1LL * power1[i - 1] * B1 % MOD1;
            power2[i] = 1LL * power2[i - 1] * B2 % MOD2;
        }

        for (int i = 0; i < n; ++i) {
            prefixHash1[i + 1] = (1LL * prefixHash1[i] * B1 + charToInt(T[i])) % MOD1;
            prefixHash2[i + 1] = (1LL * prefixHash2[i] * B2 + charToInt(T[i])) % MOD2;
        }
    }

    bool compareSubstring(int i) {
        for (int j = 0; j < P.size(); ++j) {
            if (T[i + j] != P[j]) return false;
        }
        return true;
    }

public:
    void loadData() {
        cin >> T >> P;
    }

    void execute() {
        int n = T.size(), m = P.size();
        if (m > n) {
            result = 0;
            return;
        }

        prepareHashing();

        int hashP1 = computeHash(P, B1, MOD1);
        int hashP2 = computeHash(P, B2, MOD2);

        for (int i = 0; i <= n - m; ++i) {
            int hashT1 = getHash(prefixHash1, power1, i, i + m - 1, MOD1);
            int hashT2 = getHash(prefixHash2, power2, i, i + m - 1, MOD2);
            if (hashT1 == hashP1 && hashT2 == hashP2) {
                result++;
            }
        }
    }

    void printData() {
        cout << result << "\n";
    }

    void run() {
        loadData();
        execute();
        printData();
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    Task task;
    task.run();
    return 0;
}
