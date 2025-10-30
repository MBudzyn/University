#include <iostream>
#include <vector>
using namespace std;

class SegmentTree {
private:
    int size;
    vector<long long> tree;

public:
    void build(const vector<long long>& values) {
        int n = values.size();
        size = 1;
        while (size < n) size *= 2;
        tree.assign(2 * size, 0);

        for (int i = 0; i < n; ++i)
            tree[size + i] = values[i];

        for (int i = size - 1; i > 0; --i)
            tree[i] = tree[2 * i] + tree[2 * i + 1];
    }

    void update(int pos, long long value) {
        pos += size;
        tree[pos] = value;
        for (pos /= 2; pos > 0; pos /= 2)
            tree[pos] = tree[2 * pos] + tree[2 * pos + 1];
    }

    long long query(int l, int r) {
        l += size;
        r += size;
        long long res = 0;
        while (l <= r) {
            if (l % 2 == 1) res += tree[l++];
            if (r % 2 == 0) res += tree[r--];
            l /= 2;
            r /= 2;
        }
        return res;
    }
};

class Task {
private:
    int N, Q, timer = 0;
    vector<vector<int>> adj;
    vector<int> in, out;
    vector<long long> flatTree;
    vector<long long> values;
    SegmentTree seg;

    void dfs(int v, int parent) {
        in[v] = timer++;
        flatTree[in[v]] = values[v];
        for (int u : adj[v]) {
            if (u != parent) dfs(u, v);
        }
        out[v] = timer;
    }

    void loadData() {
        cin >> N >> Q;
        adj.resize(N + 1);
        values.resize(N + 1);
        in.resize(N + 1);
        out.resize(N + 1);
        flatTree.resize(N);

        for (int i = 1; i <= N; ++i)
            cin >> values[i];

        for (int i = 0; i < N - 1; ++i) {
            int u, v;
            cin >> u >> v;
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
    }

    void answerAll() {
        while (Q--) {
            int type;
            cin >> type;
            if (type == 1) {
                int v;
                long long x;
                cin >> v >> x;
                seg.update(in[v], x);
            } else {
                int v;
                cin >> v;
                cout << seg.query(in[v], out[v] - 1) << '\n';
            }
        }
    }

public:
    void run() {
        loadData();
        dfs(1, -1);
        seg.build(flatTree);
        answerAll();
    }
};

int main() {

    Task task;
    task.run();
    return 0;
}

