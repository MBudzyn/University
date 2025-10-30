#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Node {
public:
    int height;
    int diameter;

    Node() {
        height = 0;
        diameter = 0;
    }
};

void dfs(vector<Node>& nodes, const vector<vector<int>>& adj, int node, int parent) {
    int max1 = -1, max2 = -1;

    for (int child : adj[node]) {
        if (child == parent) continue;
        dfs(nodes, adj, child, node);

        nodes[node].diameter = max(nodes[node].diameter, nodes[child].diameter);
        nodes[node].height = max(nodes[node].height, nodes[child].height + 1);

        int h = nodes[child].height;
        if (h > max1) {
            max2 = max1;
            max1 = h;
        } else if (h > max2) {
            max2 = h;
        }
    }

    if (max2 != -1) {
        nodes[node].diameter = max(nodes[node].diameter, max1 + max2 + 2);
    } else if (max1 != -1) {
        nodes[node].diameter = max(nodes[node].diameter, max1 + 1);
    }
}

int main() {
    int N;
    cin >> N;
    vector<Node> nodes(N);
    vector<vector<int>> adj(N);

    for (int i = 0; i < N - 1; i++) {
        int a, b;
        cin >> a >> b;
        --a;
        --b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }

    dfs(nodes, adj, 0, -1);

    cout << nodes[0].diameter << endl;

    return 0;
}

