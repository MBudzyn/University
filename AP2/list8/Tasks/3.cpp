#include <iostream>
#include <vector>
using namespace std;

class Task {
public:
    int N, M, Q;
    vector<int> pom_table;
    vector<int> lazy;
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
        for (int i = 0; i < two_power; i++) {
            pom_table[two_power + i] = M;
        }
    }

    void push(int node_ind, int l, int r) {
        if (lazy[node_ind] != 0) {
            pom_table[node_ind] -= lazy[node_ind];
            if (l != r) {
                lazy[2 * node_ind] += lazy[node_ind];
                lazy[2 * node_ind + 1] += lazy[node_ind];
            }
            lazy[node_ind] = 0;
        }
    }

    void update(int node_ind, pair<int, int> full_range, pair<int, int> range, int value) {
        int l = full_range.first;
        int r = full_range.second;
        push(node_ind, l, r);

        if (range.first > r || range.second < l) return;
        if (range.first <= l && r <= range.second) {
            lazy[node_ind] += value;
            push(node_ind, l, r);
            return;
        }

        int mid = (l + r) / 2;
        update(node_ind * 2, {l, mid}, range, value);
        update(node_ind * 2 + 1, {mid + 1, r}, range, value);
        pom_table[node_ind] = min(pom_table[2 * node_ind], pom_table[2 * node_ind + 1]);
    }

    int check(int node_ind, pair<int, int> full_range, pair<int, int> range) {
        int l = full_range.first;
        int r = full_range.second;
        push(node_ind, l, r);

        if (range.first > r || range.second < l) return M;

        if (range.first <= l && r <= range.second) {
            return pom_table[node_ind];
        }

        int mid = (l + r) / 2;
        int left = check(node_ind * 2, {l, mid}, range);
        int right = check(node_ind * 2 + 1, {mid + 1, r}, range);
        return min(left, right);
    }

    void solve() {
        for (int i = 0; i < Q; i++) {
            int P, K, L;
            cin >> P >> K >> L;

            int min_free = check(1, {1, two_power}, {P, K - 1});

            if (min_free >= L) {
                cout << "T\n";
                update(1, {1, two_power}, {P, K - 1}, L);
            } else {
                cout << "N\n";
            }
        }
    }

    void loadData() {
        cin >> N >> M >> Q;
        two_power = min_to_power(N);
        pom_table.assign(2 * two_power, M);
        lazy.assign(2 * two_power, 0);
        fill_default();
    }
};

int main() {
    Task t;
    return 0;
}
