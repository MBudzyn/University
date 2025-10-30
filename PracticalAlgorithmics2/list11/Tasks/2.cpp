#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class TaskSCC {
private:
    int N, M;
    vector<vector<int>> adj, adj_rev;
    vector<bool> visited;
    vector<int> order;
    vector<int> component;
    int num_components = 0;

public:
    void loadData() {
        cin >> N >> M;
        adj.resize(N + 1);
        adj_rev.resize(N + 1);

        for (int i = 0; i < M; ++i) {
            int u, v;
            cin >> u >> v;
            adj[u].push_back(v);
            adj_rev[v].push_back(u);
        }

        for (int i = 1; i <= N; ++i) {
            sort(adj[i].begin(), adj[i].end());
            sort(adj_rev[i].begin(), adj_rev[i].end());
        }
    }

    void dfs1(int u) {
        visited[u] = true;
        for (int v : adj[u]) {
            if (!visited[v]) {
                dfs1(v);
            }
        }
        order.push_back(u);
    }
    void execute() {
        visited.assign(N + 1, false);
        for (int i = 1; i <= N; ++i) {
            if (!visited[i]) {
                dfs1(i);
            }
        }

        reverse(order.begin(), order.end());

        visited.assign(N + 1, false);
        component.assign(N + 1, 0);
        vector<pair<int, vector<int>>> components;

        for (int u : order) {
            if (!visited[u]) {
                vector<int> comp;
                dfs2(u, comp);
                sort(comp.begin(), comp.end());
                components.emplace_back(comp[0], comp);
            }
        }

        sort(components.begin(), components.end());

        num_components = components.size();
        for (int i = 0; i < num_components; ++i) {
            for (int u : components[i].second) {
                component[u] = i + 1;
            }
        }
    }

    void dfs2(int u, vector<int>& comp) {
        visited[u] = true;
        comp.push_back(u);
        for (int v : adj_rev[u]) {
            if (!visited[v]) {
                dfs2(v, comp);
            }
        }
    }

    void printData() {
        cout << num_components << '\n';
        for (int i = 1; i <= N; ++i) {
            cout << component[i] << ' ';
        }
        cout << '\n';
    }

    void run() {
        loadData();
        execute();
        printData();
    }
};

int main() {

    TaskSCC task;
    task.run();
    return 0;
}
