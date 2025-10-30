#include <iostream>
#include <vector>

using namespace std;

vector<int> countDivisors(int n) {
    vector<int> divisors(n + 1, 1);
    for (int i = 2; i <= n; i++) {
        for (int j = i; j <= n; j += i) {
            divisors[j]++;
        }
    }
    return divisors;
}

int main() {
    int n;
    int max;
    cin >> n;
    vector<int> questions;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        questions.push_back(x);
        if (i == 0 || x > max) {
            max = x;
        }
    }
    vector<int> divisors = countDivisors(max);
    for (int i = 0; i < n; i++) {
        cout << divisors[questions[i]] << endl;
    }

}


