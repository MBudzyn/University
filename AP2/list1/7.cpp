#include <iostream>
#include <vector>

using namespace std;

vector<vector<int>> graph;
vector<bool> visited;
int components = 0;

void dfs(int node) {
    visited[node] = true;
    for (int neighbor : graph[node]) {
        if (!visited[neighbor]) {
            dfs(neighbor);
        }
    }
}

int main() {
    int N, M;
    cin >> N >> M;

    graph.resize(N + 1);
    visited.resize(N + 1, false);

    for (int i = 0; i < M; i++) {
        int a, b;
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    for (int i = 1; i <= N; i++) {
        if (!visited[i]) {
            dfs(i);
            components++;
        }
    }

    cout << components - 1 << endl;

    return 0;
}

