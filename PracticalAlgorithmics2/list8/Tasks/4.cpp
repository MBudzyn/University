#include <iostream>
#include <vector>
using namespace std;

struct Node {
    long long sum = 0;
    long long add_lazy = 0;
    long long set_lazy = 0;
    bool set_active = false;

    void deactivate() {
        set_active = false;
        add_lazy = 0;
        set_lazy = 0;
    }
};

class Task {
public:
    int N, Q;
    vector<Node> pom_table;
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

    void fill_default(const vector<int>& data) {
        for (int i = 0; i < N; i++) {
            pom_table[two_power + i].sum = data[i];
        }
        for (int i = two_power - 1; i > 0; i--) {
            pom_table[i].sum = pom_table[i * 2].sum + pom_table[i * 2 + 1].sum;
        }
    }

    void push(int node_ind, int l, int r) {
        Node &node = pom_table[node_ind];
        if (node.set_active) {
            apply_set(node_ind * 2, l, (l + r) / 2, node.set_lazy);
            apply_set(node_ind * 2 + 1, (l + r) / 2 + 1, r, node.set_lazy);
            node.deactivate();
        } else if (node.add_lazy != 0) {
            apply_add(node_ind * 2, l, (l + r) / 2, node.add_lazy);
            apply_add(node_ind * 2 + 1, (l + r) / 2 + 1, r, node.add_lazy);
            node.add_lazy = 0;
        }
    }

    void apply_add(int node_ind, int l, int r, long long value) {
        Node &node = pom_table[node_ind];
        if (node.set_active) {
            node.set_lazy += value;
        } else {
            node.add_lazy += value;
        }
        node.sum += value * (r - l + 1);
    }

    void apply_set(int node_ind, int l, int r, long long value) {
        Node &node = pom_table[node_ind];
        node.set_active = true;
        node.set_lazy = value;
        node.add_lazy = 0;
        node.sum = value * (r - l + 1);
    }

    void update(int node_ind, pair<int, int> full_range, pair<int, int> range, long long value, int type) {
        if (range.first == full_range.first && range.second == full_range.second) {
            if (type == 1) apply_add(node_ind, full_range.first, full_range.second, value);
            else apply_set(node_ind, full_range.first, full_range.second, value);
            return;
        }

        push(node_ind, full_range.first, full_range.second);
        int mid = (full_range.first + full_range.second) / 2;

        if (range.second <= mid) {
            update(node_ind * 2, {full_range.first, mid}, range, value, type);
        } else if (range.first > mid) {
            update(node_ind * 2 + 1, {mid + 1, full_range.second}, range, value, type);
        } else {
            update(node_ind * 2, {full_range.first, mid}, {range.first, mid}, value, type);
            update(node_ind * 2 + 1, {mid + 1, full_range.second}, {mid + 1, range.second}, value, type);
        }

        pom_table[node_ind].sum = pom_table[node_ind * 2].sum + pom_table[node_ind * 2 + 1].sum;
    }

    long long query(int node_ind, pair<int, int> full_range, pair<int, int> range) {
        if (range.first > range.second || full_range.first > full_range.second) return 0;
        if (range.first == full_range.first && range.second == full_range.second) {
            return pom_table[node_ind].sum;
        }

        push(node_ind, full_range.first, full_range.second);
        int mid = (full_range.first + full_range.second) / 2;

        if (range.second <= mid) {
            return query(node_ind * 2, {full_range.first, mid}, range);
        } else if (range.first > mid) {
            return query(node_ind * 2 + 1, {mid + 1, full_range.second}, range);
        } else {
            return query(node_ind * 2, {full_range.first, mid}, {range.first, mid}) +
                   query(node_ind * 2 + 1, {mid + 1, full_range.second}, {mid + 1, range.second});
        }
    }

    void solve() {
        for (int i = 0; i < Q; i++) {
            int type, x, y;
            cin >> type >> x >> y;
            x--, y--;
            if (type == 1 || type == 2) {
                int v; cin >> v;
                update(1, {0, two_power - 1}, {x, y}, v, type);
            } else if (type == 3) {
                cout << query(1, {0, two_power - 1}, {x, y})<<endl;
            }
        }
    }

    void loadData() {
        cin >> N >> Q;
        two_power = min_to_power(N);
        pom_table.resize(2 * two_power);
        vector<int> data(N);
        for (int i = 0; i < N; i++) {
            cin >> data[i];
        }
        fill_default(data);
    }
};

int main() {

    Task t;
    return 0;
}
