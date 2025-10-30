#include <iostream>
#include <vector>

using namespace std;
const int LOG = 20;

class Node {
public:
    int depth;
    vector<int> up;

    Node() {
        depth = 0;
        up.assign(LOG, -1);
    }
};

class Task2 {
private:
    int N, Q;
    vector<Node> nodes;
    vector<vector<int>> adj;
    vector<pair<int, int>> queries;

    void dfs(int v, int parent) {
        nodes[v].up[0] = parent;
        for (int i = 1; i < LOG; i++) {
            int mid = nodes[v].up[i - 1];
            if (mid != -1) {
                nodes[v].up[i] = nodes[mid].up[i - 1];
            }
        }

        for (int child : adj[v]) {
            if (child == parent) continue;
            nodes[child].depth = nodes[v].depth + 1;
            dfs(child, v);
        }
    }

    int liftNode(int v, int k) const {
        for (int i = 0; i < LOG; i++) {
            if (k & (1 << i)) {
                v = nodes[v].up[i];
                if (v == -1) return -1;
            }
        }
        return v;
    }

    int getLCA(int u, int v) const {
        if (nodes[u].depth < nodes[v].depth) swap(u, v);

        u = liftNode(u, nodes[u].depth - nodes[v].depth);
        if (u == v) return u;

        for (int i = LOG - 1; i >= 0; i--) {
            if (nodes[u].up[i] != -1 && nodes[u].up[i] != nodes[v].up[i]) {
                u = nodes[u].up[i];
                v = nodes[v].up[i];
            }
        }

        return nodes[u].up[0];
    }

public:

    void loadData() {
        cin >> N >> Q;
        nodes.resize(N);
        adj.resize(N);

        for (int i = 1; i < N; i++) {
            int p;
            cin >> p;
            --p;
            adj[p].push_back(i);
            adj[i].push_back(p);
        }

        queries.resize(Q);
        for (int i = 0; i < Q; ++i) {
            int u, v;
            cin >> u >> v;
            queries[i] = {u - 1, v - 1};
        }
    }

    void preprocess() {
        dfs(0, -1);
    }

    void solve() const {
        for (const auto& [u, v] : queries) {
            int lca = getLCA(u, v);
            cout << lca + 1 << '\n';
        }
    }

    void run() {
        loadData();
        preprocess();
        solve();
    }
};

int main() {
    Task2 task;
    task.run();

    return 0;
}

