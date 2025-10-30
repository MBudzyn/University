#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>

using namespace std;

class TaskEulerianCycle {
private:
    int N, M;
    vector<vector<pair<int, int>>> adj;
    vector<bool> used;
    vector<int> degree;
    vector<int> path;
    bool possible = true;

public:
    void loadData() {
        cin >> N >> M;
        adj.resize(N + 1);
        degree.assign(N + 1, 0);
        used.assign(M, false);

        for (int i = 0; i < M; ++i) {
            int u, v;
            cin >> u >> v;
            adj[u].emplace_back(v, i);
            adj[v].emplace_back(u, i);
            degree[u]++;
            degree[v]++;
        }
    }

    bool isConnected() {
        vector<bool> visited(N + 1, false);
        stack<int> s;
        s.push(1);
        visited[1] = true;

        while (!s.empty()) {
            int u = s.top(); s.pop();
            for (auto [v, id] : adj[u]) {
                if (!visited[v]) {
                    visited[v] = true;
                    s.push(v);
                }
            }
        }

        for (int i = 1; i <= N; ++i) {
            if (!adj[i].empty() && !visited[i])
                return false;
        }
        return true;
    }

    void dfs(int u) {
        while (!adj[u].empty()) {
            auto [v, id] = adj[u].back();
            adj[u].pop_back();
            if (used[id]) continue;
            used[id] = true;
            dfs(v);
        }
        path.push_back(u);
    }

    void execute() {
        for (int i = 1; i <= N; ++i) {
            if (degree[i] % 2 != 0) {
                possible = false;
                return;
            }
        }

        if (!isConnected()) {
            possible = false;
            return;
        }

        dfs(1);

        if ((int)path.size() != M + 1) {
            possible = false;
        }
    }

    void printData() {
        if (!possible) {
            cout << "IMPOSSIBLE\n";
        } else {
            reverse(path.begin(), path.end());
            for (int v : path)
                cout << v << " ";
            cout << '\n';
        }
    }

    void run() {
        loadData();
        execute();
        printData();
    }
};

int main() {
    TaskEulerianCycle task;
    task.run();

    return 0;
}
