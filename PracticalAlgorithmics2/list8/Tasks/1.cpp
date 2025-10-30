#include <iostream>
#include <vector>
using namespace std;


class Task {
public:
    int N, Q;
    vector<int> pom_table;
    int two_power;

    Task() {
        run();
    }

    int min_to_power(int n) {
        int i = 1;
        while (i < n) {
            i *= 2;
        }
        return i;
    }

    void run() {
        loadData();
        solve();
    }

    void fill_default() {
        for (int i = two_power - 1; i > 0; i--) {
            pom_table[i] = max(pom_table[left_child(i)], pom_table[right_child(i)]);
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

    void update(int index, int new_val) {
        int par = two_power + index;
        pom_table[par] -= new_val;
        while (par > 1) {
            par = parent(par);
            int left = left_child(par);
            int right = right_child(par);

            pom_table[par] = max(pom_table[left], pom_table[right]);
        }
    }

    int answer(int value) {
        if (pom_table[1] < value) return 0;

        int index = 1;
        while (index < two_power) {
            int left = left_child(index);
            if (pom_table[left] >= value) {
                index = left;
            } else {
                index = right_child(index);
            }
        }
        return index - two_power + 1;
    }


    void solve() {
        for (int i = 0; i < Q; i++) {
            int new_val;
            cin >> new_val;
            int index = answer(new_val);
            cout << index << " ";
            if (index != 0) {
                update(index - 1, new_val);
            }
        }
        cout << endl;
    }

    void loadData() {
        cin >> N >> Q;
        two_power = min_to_power(N);
        pom_table.resize(2 * two_power, 0);
        for (int i = 0; i < N; i++) {
            int x;
            cin >> x;
            pom_table[two_power + i] = x;
        }
        fill_default();
    }
};

int main() {
    Task t;
    return 0;
}

