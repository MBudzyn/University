#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class MaxCoins {
private:
    int N, M;
    vector<int> coins;
    vector<vector<int>> adj, adj_rev;
    vector<bool> visited;
    vector<int> order, component;
    int num_components = 0;
    vector<long long> scc_coins;
    vector<vector<int>> dag;

public:
    void loadData() {
        cin >> N >> M;
        coins.resize(N + 1);
        adj.resize(N + 1);
        adj_rev.resize(N + 1);
        for (int i = 1; i <= N; ++i) {
            cin >> coins[i];
        }
        for (int i = 0; i < M; ++i) {
            int u, v; cin >> u >> v;
            adj[u].push_back(v);
            adj_rev[v].push_back(u);
        }
    }

    void dfs1(int u) {
        visited[u] = true;
        for (int v : adj[u])
            if (!visited[v])
                dfs1(v);
        order.push_back(u);
    }

    void dfs2(int u) {
        visited[u] = true;
        component[u] = num_components;
        scc_coins[num_components] += coins[u];
        for (int v : adj_rev[u])
            if (!visited[v])
                dfs2(v);
    }

    void findSCC() {
        visited.assign(N + 1, false);
        for (int i = 1; i <= N; ++i)
            if (!visited[i])
                dfs1(i);

        reverse(order.begin(), order.end());

        visited.assign(N + 1, false);
        component.assign(N + 1, 0);
        num_components = 0;
        scc_coins.clear();

        for (int u : order) {
            if (!visited[u]) {
                scc_coins.push_back(0);
                dfs2(u);
                num_components++;
            }
        }
    }

    void buildDAG() {
        dag.assign(num_components, vector<int>());
        for (int u = 1; u <= N; ++u) {
            for (int v : adj[u]) {
                int cu = component[u];
                int cv = component[v];
                if (cu != cv) {
                    dag[cu].push_back(cv);
                }
            }
        }
    }

    long long solve() {
        vector<long long> dp(num_components, 0);
        vector<int> indeg(num_components, 0);

        for (int u = 0; u < num_components; ++u) {
            for (int v : dag[u])
                indeg[v]++;
        }

        vector<int> q;
        for (int i = 0; i < num_components; ++i)
            if (indeg[i] == 0) {
                dp[i] = scc_coins[i];
                q.push_back(i);
            }

        int pos = 0;
        while (pos < (int)q.size()) {
            int u = q[pos++];
            for (int v : dag[u]) {
                if (dp[u] + scc_coins[v] > dp[v]) {
                    dp[v] = dp[u] + scc_coins[v];
                }
                indeg[v]--;
                if (indeg[v] == 0)
                    q.push_back(v);
            }
        }

        return *max_element(dp.begin(), dp.end());
    }

    void run() {
        loadData();
        findSCC();
        buildDAG();
        cout << solve() << "\n";
    }
};

int main() {
    MaxCoins task;
    task.run();
    return 0;
}
