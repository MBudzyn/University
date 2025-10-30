#include <iostream>
#include <vector>

using namespace std;

class DSU {
public:
    vector<int> parent, rank;
    vector<bool> parity;

    DSU(int n) {
        parent.resize(n);
        rank.resize(n, 0);
        parity.resize(n, false);
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
    }

    int find(int x) {
        if (parent[x] != x) {
            int root = find(parent[x]);
            parity[x] = parity[x] ^ parity[parent[x]];
            parent[x] = root;
        }
        return parent[x];
    }

    bool unionSets(int a, int b, bool p) {
        int rootA = find(a);
        int rootB = find(b);

        if (rootA == rootB) {
            return (parity[a] ^ parity[b]) == p;
        }

        if (rank[rootA] < rank[rootB]) {
            swap(rootA, rootB);
        }

        parent[rootB] = rootA;
        parity[rootB] = parity[a] ^ parity[b] ^ p;

        if (rank[rootA] == rank[rootB]) {
            rank[rootA]++;
        }

        return true;
    }
};

int main() {
    int N, M;
    cin >> N >> M;

    DSU dsu(N);

    for (int i = 0; i < M; i++) {
        int a, b, p;
        cin >> a >> b >> p;
        a--; b--;

        if (!dsu.unionSets(a, b, p)) {
            cout << i << endl;
            return 0;
        }
    }

    cout << M << endl;
    return 0;
}



