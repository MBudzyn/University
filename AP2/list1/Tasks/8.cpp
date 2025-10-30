#include <iostream>
#include <vector>

using namespace std;

vector<vector<int>> graph;
vector<int> val;


void bfs(int start) {
    vector<int> queue;
    queue.push_back(start);
    val[start] = 0;

    while (!queue.empty()) {
        int node = queue.front();
        queue.erase(queue.begin());

        for (int neighbor : graph[node]) {
            if (val[neighbor] == -1) {
                val[neighbor] = val[node] + 1;
                queue.push_back(neighbor);
            }
        }
    }
}


int main() {
    int N, M;
    cin >> N >> M;

    graph.resize(N + 1);
    val.resize(N + 1, -1);

    for (int i = 0; i < M; i++) {
        int a, b;
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    bfs(1);
    for (int i = 2; i <= N; i++) {
        cout << val[i] << " ";
    }

    return 0;
}

