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

class Task1 {
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

    int getKthAncestor(int v, int k) const {
        for (int i = 0; i < LOG; i++) {
            if (k & (1 << i)) {
                v = nodes[v].up[i];
                if (v == -1) return -1;
            }
        }
        return v;
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
            int v, k;
            cin >> v >> k;
            queries[i] = {v - 1, k};
        }
    }

    void preprocess() { dfs(0, -1);}

    void solve() const {
        for (const auto& [v, k] : queries) {
            int ans = getKthAncestor(v, k);
            if (ans == -1)
                cout << -1 << '\n';
            else
                cout << ans + 1 << '\n';
        }
    }

    void run() {
        loadData();
        preprocess();
        solve();
    }
};

int main() {
    Task1 task;
    task.run();

    return 0;
}
