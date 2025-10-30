#include <iostream>
#include <vector>
#include <queue>
#include <climits>
#include <tuple>

using namespace std;

class Task2 {
private:
    int N, M;
    vector<vector<pair<int, long long>>> adj;
    vector<vector<long long>> dist;

public:
    void loadData() {
        cin >> N >> M;
        adj.resize(N + 1);
        dist.assign(N + 1, vector<long long>(2, LLONG_MAX));

        for (int i = 0; i < M; ++i) {
            int u, v;
            long long w;
            cin >> u >> v >> w;
            adj[u].emplace_back(v, w);
        }
    }

    void execute() {
        priority_queue<tuple<long long, int, int>,
                vector<tuple<long long, int, int>>,
                greater<>> pq;

        dist[1][0] = 0;
        pq.emplace(0, 1, 0);

        while (!pq.empty()) {
            auto [curr_dist, u, used_coupon] = pq.top();
            pq.pop();

            if (curr_dist > dist[u][used_coupon]) continue;

            for (auto &[v, w] : adj[u]) {
                if (dist[u][used_coupon] + w < dist[v][used_coupon]) {
                    dist[v][used_coupon] = dist[u][used_coupon] + w;
                    pq.emplace(dist[v][used_coupon], v, used_coupon);
                }

                if (!used_coupon) {
                    long long discounted = w / 2;
                    if (dist[u][0] + discounted < dist[v][1]) {
                        dist[v][1] = dist[u][0] + discounted;
                        pq.emplace(dist[v][1], v, 1);
                    }
                }
            }
        }
    }

    void printData() {
        cout << min(dist[N][0], dist[N][1]) << '\n';
    }

    void run() {
        loadData();
        execute();
        printData();
    }
};

int main() {
    Task2 task;
    task.run();
    return 0;
}
