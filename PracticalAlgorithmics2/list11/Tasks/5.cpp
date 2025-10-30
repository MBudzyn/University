#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>
#include <utility>
using namespace std;

class Task {
private:
    int N, M;
    vector<vector<pair<int, int>>> adj;
    vector<int> indeg, outdeg;
    vector<bool> used;
    vector<int> path;
    bool possible = true;

public:
    void loadData() {
        cin >> N >> M;
        adj.resize(N + 1);
        indeg.assign(N + 1, 0);
        outdeg.assign(N + 1, 0);
        used.assign(M, false);

        for (int i = 0; i < M; ++i) {
            int u, v;
            cin >> u >> v;
            adj[u].emplace_back(v, i);
            outdeg[u]++;
            indeg[v]++;
        }

        for (int u = 1; u <= N; ++u) {
            reverse(adj[u].begin(), adj[u].end());
        }
    }

    void dfs(int start) {
        stack<int> st;
        st.push(start);
        vector<int> result;

        while (!st.empty()) {
            int u = st.top();
            while (!adj[u].empty() && used[adj[u].back().second]) {
                adj[u].pop_back();
            }
            if (!adj[u].empty()) {
                auto [v, id] = adj[u].back();
                adj[u].pop_back();
                used[id] = true;
                st.push(v);
            } else {
                result.push_back(u);
                st.pop();
            }
        }

        if ((int)result.size() == M + 1) {
            reverse(result.begin(), result.end());
            path = result;
        } else {
            possible = false;
        }
    }

    void execute() {
        if (outdeg[1] != indeg[1] + 1 || indeg[N] != outdeg[N] + 1) {
            possible = false;
            return;
        }
        for (int i = 1; i <= N; ++i) {
            if (i != 1 && i != N && indeg[i] != outdeg[i]) {
                possible = false;
                return;
            }
        }
        dfs(1);
        if (path.empty() || path.back() != N) {
            possible = false;
        }
    }

    void printData() {
        if (!possible) {
            cout << "IMPOSSIBLE\n";
            return;
        }
        for (int v : path) cout << v << " ";
        cout << "\n";
    }

    void run() {
        loadData();
        execute();
        printData();
    }
};

int main() {

    Task task;
    task.run();
    return 0;
}
