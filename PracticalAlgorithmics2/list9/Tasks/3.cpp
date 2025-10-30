#include <iostream>
#include <vector>

using namespace std;
const int LOG = 20;

class Node {
public:
    int depth;
    vector<int> up;
    int mod;
    int result;

    Node() {
        depth = 0;
        up.assign(LOG, -1);
        mod = 0;
        result = 0;
    }
};

class Task3 {
private:
    int N, M;
    vector<Node> nodes;
    vector<vector<int>> adj;
    vector<pair<int, int>> paths;

    void dfs(int v, int parent) {
        nodes[v].up[0] = parent;
        for (int i = 1; i < LOG; i++) {
            int mid = nodes[v].up[i - 1];
            if (mid != -1)
                nodes[v].up[i] = nodes[mid].up[i - 1];
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

    void propagate(int v, int parent) {
        for (int child : adj[v]) {
            if (child == parent) continue;
            propagate(child, v);
            nodes[v].mod += nodes[child].mod;
        }
        nodes[v].result = nodes[v].mod;
    }

public:
    void loadData() {
        cin >> N >> M;
        nodes.resize(N);
        adj.resize(N);

        for (int i = 0; i < N - 1; i++) {
            int u, v;
            cin >> u >> v;
            --u; --v;
            adj[u].push_back(v);
            adj[v].push_back(u);
        }

        paths.resize(M);
        for (int i = 0; i < M; ++i) {
            int u, v;
            cin >> u >> v;
            paths[i] = {u - 1, v - 1};
        }
    }

    void preprocess() {
        dfs(0, -1);
    }

    void applyModifications() {
        for (const auto& [u, v] : paths) {
            int lca = getLCA(u, v);
            nodes[u].mod += 1;
            nodes[v].mod += 1;
            nodes[lca].mod -= 1;
            int parent = nodes[lca].up[0];
            if (parent != -1) {
                nodes[parent].mod -= 1;
            }
        }
    }

    void solve() {
        for (int i = 0; i < N; i++) {
            cout << nodes[i].result << ' ';
        }
        cout << '\n';
    }

    void run() {
        loadData();
        preprocess();
        applyModifications();
        propagate(0, -1);
        solve();
    }
};

int main() {
    Task3 task;
    task.run();

    return 0;
}

