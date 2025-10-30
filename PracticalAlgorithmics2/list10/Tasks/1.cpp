#include <iostream>
#include <vector>
#include <queue>
#include <climits>

using namespace std;

class Task1 {
private:
    int N, M;
    vector<vector<pair<int, long long>>> adj;
    vector<long long> dist;

public:
    void loadData() {
        cin >> N >> M;
        adj.resize(N + 1);
        dist.assign(N + 1, LLONG_MAX);

        for (int i = 0; i < M; ++i) {
            int u, v;
            long long w;
            cin >> u >> v >> w;
            adj[u].emplace_back(v, w);
        }
    }

    void execute() {
        priority_queue<pair<long long, int>,
                vector<pair<long long, int>>, greater<>> pq;
        dist[1] = 0;
        pq.push({0, 1});

        while (!pq.empty()) {
            long long d = pq.top().first;
            int u = pq.top().second;
            pq.pop();

            if (d > dist[u]) continue;

            for (auto& edge : adj[u]) {
                int v = edge.first;
                long long w = edge.second;

                if (dist[u] + w < dist[v]) {
                    dist[v] = dist[u] + w;
                    pq.push({dist[v], v});
                }
            }
        }
    }

    void printData() {
        for (int i = 1; i <= N; ++i) {
            if (dist[i] == LLONG_MAX) {
                cout << -1 << " ";
            } else {
                cout << dist[i] << " ";
            }
        }
        cout << endl;
    }

    void run() {
        loadData();
        execute();
        printData();
    }
};

int main() {
    Task1 task;
    task.run();

    return 0;
}


