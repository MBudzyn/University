#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Task4 {
public:
    int N, M;

    struct Edge {
        int u, v;
        long long w;
    };

    vector<Edge> edges;
    vector<long long> dist;
    vector<int> parent;

    void read_input() {
        cin >> N >> M;
        edges.resize(M);
        for (int i = 0; i < M; ++i) {
            cin >> edges[i].u >> edges[i].v >> edges[i].w;
            edges[i].u--;
            edges[i].v--;
        }
    }

    int relax_edges() {
        dist.assign(N, 0);
        parent.assign(N, -1);
        int last_updated = -1;

        for (int i = 0; i < N; ++i) {
            last_updated = -1;
            for (const auto& e : edges) {
                if (dist[e.u] + e.w < dist[e.v]) {
                    dist[e.v] = dist[e.u] + e.w;
                    parent[e.v] = e.u;
                    last_updated = e.v;
                }
            }
        }
        return last_updated;
    }

    int get_cycle_start(int last_updated) {
        int x = last_updated;
        for (int i = 0; i < N; ++i) {
            x = parent[x];
        }
        return x;
    }

    vector<int> extract_cycle(int start) {
        vector<int> cycle;
        int curr = start;
        do {
            cycle.push_back(curr);
            curr = parent[curr];
        } while (curr != start && cycle.size() <= N);
        cycle.push_back(start);
        reverse(cycle.begin(), cycle.end());
        return cycle;
    }

    void print_cycle(const vector<int>& cycle) {
        cout << "YES\n";
        for (int v : cycle) {
            cout << (v + 1) << " ";
        }
        cout << "\n";
    }

    void find_negative_cycle() {
        int last_updated = relax_edges();

        if (last_updated == -1) {
            cout << "NO\n";
            return;
        }

        int start = get_cycle_start(last_updated);
        vector<int> cycle = extract_cycle(start);
        print_cycle(cycle);
    }

    void run() {
        read_input();
        find_negative_cycle();
    }
};

int main() {
    Task4 task;
    task.run();
    return 0;
}
