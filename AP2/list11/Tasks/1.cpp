#include <iostream>
#include <vector>
#include <queue>

using namespace std;

class TaskTopSort {
private:
    int N, M;
    vector<vector<int>> adj;
    vector<int> indegree;
    vector<int> result;

public:
    void loadData() {
        cin >> N >> M;
        adj.resize(N + 1);
        indegree.assign(N + 1, 0);

        for (int i = 0; i < M; ++i) {
            int u, v;
            cin >> u >> v;
            adj[u].push_back(v);
            indegree[v]++;
        }
    }

    void execute() {
        priority_queue<int, vector<int>, greater<>> pq;

        for (int i = 1; i <= N; ++i) {
            if (indegree[i] == 0) {
                pq.push(i);
            }
        }

        while (!pq.empty()) {
            int u = pq.top();
            pq.pop();
            result.push_back(u);

            for (int v : adj[u]) {
                indegree[v]--;
                if (indegree[v] == 0) {
                    pq.push(v);
                }
            }
        }
    }

    void printData() {
        if ((int)result.size() != N) {
            cout << "IMPOSSIBLE\n";
            return;
        }

        for (int v : result) {
            cout << v << " ";
        }
        cout << "\n";
    }

    void run() {
        loadData();
        execute();
        printData();
    }
};

int main() {
    TaskTopSort task;
    task.run();

    return 0;
}

