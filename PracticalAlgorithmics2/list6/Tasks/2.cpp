#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Node {
public:
    int maximalMatching;
    int maximalMatchingWithoutRoot;

    Node() {
        maximalMatching = 0;
        maximalMatchingWithoutRoot = 0;
    }
};

void dfs(vector<Node>& nodes, const vector<vector<int>>& adj, int node, int parent) {

    for (int child : adj[node]) {
        if (child == parent) continue;
        dfs(nodes, adj, child, node);
    }
    int sumWithoutRoot = 0;
    bool plusOne = false;
    for (int child : adj[node]) {
        if (child == parent) continue;
        sumWithoutRoot += nodes[child].maximalMatching;
        if (nodes[child].maximalMatchingWithoutRoot == nodes[child].maximalMatching) {
            plusOne = true;
        }
    }
    nodes[node].maximalMatchingWithoutRoot = sumWithoutRoot;
    if (plusOne) {
        nodes[node].maximalMatching = sumWithoutRoot + 1;
    } else { nodes[node].maximalMatching = sumWithoutRoot;}

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

    cout << nodes[0].maximalMatching << endl;

    return 0;
}

