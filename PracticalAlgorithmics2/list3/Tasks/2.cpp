#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

class Node {
public:
    unordered_set<int> colors;
    vector<int> children;
    int size;

    Node(int color) {
        colors.insert(color);
    }

    void extendColors(Node& child) {
        if (colors.size() < child.colors.size()) {
            swap(colors, child.colors);
        }
        colors.insert(child.colors.begin(), child.colors.end());
    }
};

void dfs(vector<Node>& nodes, vector<vector<int>>& adj, int node, int parent) {
    for (int child : adj[node]) {
        if (child == parent) continue;
        dfs(nodes, adj, child, node);
        nodes[child].size = nodes[child].colors.size();
        nodes[node].extendColors(nodes[child]);
        nodes[child].colors = unordered_set<int>();

    }
}

int main() {
    int N;
    cin >> N;
    vector<Node> nodes;
    for (int i = 0; i < N; i++) {
        int color;
        cin >> color;
        nodes.emplace_back(color);
    }

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

    nodes[0].size = nodes[0].colors.size();
    for (Node& node : nodes) {
        cout << node.size << " ";
    }

    return 0;
}


