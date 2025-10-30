#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class SegmentTree {
private:
    vector<int> pom_table;
    vector<int> eulerDepth;
    vector<int> euler;
    int two_power = 1;

    int combine(int a, int b) {
        if (a == -1) return b;
        if (b == -1) return a;
        return (eulerDepth[a] < eulerDepth[b]) ? a : b;
    }

public:
    void build(const vector<int>& eulerTour, const vector<int>& depthTour) {
        euler = eulerTour;
        eulerDepth = depthTour;
        int N = euler.size();

        while (two_power < N) two_power *= 2;
        pom_table.assign(2 * two_power, -1);

        for (int i = 0; i < N; ++i) {
            pom_table[two_power + i] = i;
        }

        for (int i = two_power - 1; i > 0; --i) {
            int left = pom_table[2 * i];
            int right = pom_table[2 * i + 1];
            pom_table[i] = combine(left, right);
        }
    }

    int query(int l, int r) {
        l += two_power;
        r += two_power;
        int res = -1;

        while (l <= r) {
            if (l % 2 == 1) res = combine(res, pom_table[l++]);
            if (r % 2 == 0) res = combine(res, pom_table[r--]);
            l /= 2;
            r /= 2;
        }

        return res;
    }

    int getLCA(int u, int v, const vector<int>& first) {
        int l = first[u], r = first[v];
        if (l > r) swap(l, r);
        int idx = query(l, r);
        return euler[idx];
    }
};

class Task {
private:
    int N, Q;
    vector<vector<int>> adj;
    vector<int> depth;
    vector<int> first;
    vector<int> euler, eulerDepth;
    SegmentTree seg;

    void dfs(int v, int parent, int d) {
        depth[v] = d;
        first[v] = euler.size();
        euler.push_back(v);
        eulerDepth.push_back(d);

        for (int u : adj[v]) {
            if (u == parent) continue;
            dfs(u, v, d + 1);
            euler.push_back(v);
            eulerDepth.push_back(d);
        }
    }

    void loadData() {
        cin >> N >> Q;
        adj.resize(N + 1);
        depth.resize(N + 1);
        first.resize(N + 1);

        for (int i = 0; i < N - 1; i++) {
            int u, v;
            cin >> u >> v;
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
    }

    void answer() {
        int u, v;
        cin >> u >> v;
        int lca = seg.getLCA(u, v, first);
        int dist = depth[u] + depth[v] - 2 * depth[lca];
        cout << dist << '\n';
    }

    void answerAll() {
        while (Q--) {
            answer();
        }
    }

public:
    void run() {
        loadData();
        dfs(1, -1, 0);
        seg.build(euler, eulerDepth);
        answerAll();
    }
};
int main() {
    Task task;
    task.run();
    return 0;
}
