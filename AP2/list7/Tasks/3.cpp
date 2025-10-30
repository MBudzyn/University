#include <iostream>
#include <vector>
using namespace std;

struct Node {
    long long sum;
    long long max_pref;
    long long max_suff;
    long long max_sum;

    Node(long long val = 0) {
        sum = val;
        max_pref = val;
        max_suff = val;
        max_sum = val;
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
            pom_table[i] = merge(pom_table[i * 2], pom_table[i * 2 + 1]);
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


    static Node merge(const Node& left, const Node& right) {
        Node res;
        res.sum = left.sum + right.sum;
        res.max_pref = max(left.max_pref, left.sum + right.max_pref);
        res.max_suff = max(right.max_suff, right.sum + left.max_suff);
        res.max_sum = max(left.max_sum, max(right.max_sum, left.max_suff + right.max_pref));
        return res;
    }

    void update(int index, int new_val) {
        int par = two_power + index;
        pom_table[par] = Node(new_val);
        while (par > 1) {
            par = parent(par);
            int left = left_child(par);
            int right = right_child(par);

            pom_table[par] = merge(pom_table[left], pom_table[right]);
        }
    }

    void answer_full() {
        cout << max(0LL, pom_table[1].max_sum) << endl;
    }

    void solve() {
        for (int i = 0; i < Q; i++) {
            int index, new_val;
            cin >> index >> new_val;
            index--;
            update(index, new_val);
            answer_full();
        }
    }

    void loadData() {
        cin >> N >> Q;
        two_power = min_to_power(N);
        pom_table.resize(2 * two_power, Node(0));
        for (int i = 0; i < N; i++) {
            int x;
            cin >> x;
            pom_table[two_power + i] = Node(x);
        }
        fill_default();
    }
};

int main() {
    Task t;
    return 0;
}

