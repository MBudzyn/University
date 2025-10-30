#include <iostream>
#include <vector>

using namespace std;

vector<vector<int>> tree;
vector<int> subtree_size;

void dfs(int node) {
    subtree_size[node] = 1;
    for (int child : tree[node]) {
        dfs(child);
        subtree_size[node] += subtree_size[child];
    }
}

int readInput(){
    int N;
    cin >> N;

    tree.resize(N + 1);
    subtree_size.resize(N + 1, 0);

    for (int i = 2; i <= N; i++) {
        int parent;
        cin >> parent;
        tree[parent].push_back(i);
    }
    return N;
}

void writeOutput(int N){
    for (int i = 1; i <= N; i++) {
        cout << subtree_size[i] - 1 << " ";
    }
    cout << endl;
}

int main() {
    int N;
    N = readInput();
    dfs(1);
    writeOutput(N);

    return 0;
}

