#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

class Task {
public:
    int N, M, Q;
    const long long INF = LLONG_MAX;
    vector<vector<long long>> dist;
    vector<pair<int, int>> queries;

    void loadData() {
        cin >> N >> M >> Q;
        dist.assign(N, vector<long long>(N, INF));

        for (int i = 0; i < N; ++i) {
            dist[i][i] = 0;
        }

        for (int i = 0; i < M; ++i) {
            int u, v;
            long long w;
            cin >> u >> v >> w;
            --u; --v;
            dist[u][v] = min(dist[u][v], w);
            dist[v][u] = min(dist[v][u], w);
        }

        for (int i = 0; i < Q; ++i) {
            int u, v;
            cin >> u >> v;
            --u; --v;
            queries.emplace_back(u, v);
        }
    }

    void compute_shortest_paths() {
        for (int k = 0; k < N; ++k) {
            for (int i = 0; i < N; ++i) {
                for (int j = 0; j < N; ++j) {
                    if (dist[i][k] < INF && dist[k][j] < INF) {
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
                    }
                }
            }
        }
    }

    void answer_queries() {
        for (const auto& [u, v] : queries) {
            if (dist[u][v] == INF) {
                cout << -1 << "\n";
            } else {
                cout << dist[u][v] << "\n";
            }
        }
    }
    void run(){
        loadData();
        compute_shortest_paths();
        answer_queries();
    }
};

int main() {

    Task task;
    task.run();

    return 0;
}
