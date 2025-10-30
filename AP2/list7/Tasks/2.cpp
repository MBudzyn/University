#include <iostream>
#include <vector>
using namespace std;

struct Node {
    long long sum;
    long long max_pref;
};

class Task {
public:
    int N, Q;
    vector<Node> pom_table;
    int two_power = 0;

    Task() {
        run();
    }

    void run() {
        loadData();
        solve();
    }

    int get_smallest_two_power() const {
        int i = 1;
        while (i < N) {
            i *= 2;
        }
        return i;
    }

    static int get_parent(int index) {
        return index / 2;
    }

    int get_index(int org_index) {
        return this->two_power + org_index;
    }

    Node answer(int node_ind, pair<int, int> full_range, pair<int, int> range) {
        if (range.first == full_range.first && range.second == full_range.second) {
            return pom_table[node_ind];
        }
        int mid = (full_range.first + full_range.second) / 2;

        if (range.second <= mid) {
            return answer(node_ind * 2, {full_range.first, mid}, range);
        } else if (range.first > mid) {
            return answer(node_ind * 2 + 1, {mid + 1, full_range.second}, range);
        } else {
            Node left = answer(node_ind * 2, {full_range.first, mid}, {range.first, mid});
            Node right = answer(node_ind * 2 + 1, {mid + 1, full_range.second}, {mid + 1, range.second});
            return {left.sum + right.sum, max(left.max_pref, left.sum + right.max_pref)};
        }
    }

    void update(int index, int new_val) {
        int node_ind = get_index(index);
        pom_table[node_ind] = {new_val, new_val};
        while (node_ind > 1) {
            node_ind = get_parent(node_ind);
            pom_table[node_ind].sum = pom_table[node_ind * 2].sum + pom_table[node_ind * 2 + 1].sum;
            pom_table[node_ind].max_pref = max(pom_table[node_ind * 2].max_pref,
                                               pom_table[node_ind * 2].sum + pom_table[node_ind * 2 + 1].max_pref);
        }
    }

    void answer_full(int left, int right) {
        Node res = answer(1, {0, two_power -1}, {left, right});
        cout << max(res.max_pref, 0LL) << endl;
    }

    void solve() {
        for (int i = 0; i < Q; i++) {
            int type;
            cin >> type;
            if (type == 1) {
                int index, value;
                cin >> index >> value;
                index -= 1;
                update(index, value);
            } else {
                int left, right;
                cin >> left >> right;
                answer_full(left - 1, right - 1);
            }
        }
    }

    void loadData() {
        cin >> N >> Q;
        two_power = get_smallest_two_power();
        pom_table.resize(2 * two_power + 1, Node(0,0));
        for (int i = 0; i < N; i++) {
            int x;
            cin >> x;
            pom_table[get_index(i)] = {x, x};
        }
        for (int i = two_power - 1; i >= 0; i--) {
            pom_table[i].sum = pom_table[i * 2].sum + pom_table[i * 2 + 1].sum;
            pom_table[i].max_pref = max(pom_table[i * 2].max_pref, pom_table[i * 2].sum + pom_table[i * 2 + 1].max_pref);
        }
    }
};

int main() {
    Task t;
    return 0;
}

