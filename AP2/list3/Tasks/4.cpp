#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class DSU {
public:
    vector<int> parent, rank, size, maxi, mini, edges;
    int components;

    DSU(int n) {
        parent.resize(n);
        rank.resize(n, 0);
        size.resize(n, 1);
        maxi.resize(n);
        mini.resize(n);
        edges.resize(n);
        components = n;
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            maxi[i] = i + 1;
            mini[i] = i + 1;
            edges[i] = 0;
        }
    }

    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    void unionSets(int a, int b) {
        int rootA = find(a);
        int rootB = find(b);

        if (rootA != rootB) {
            if (rank[rootA] < rank[rootB]) {
                swap(rootA, rootB);
            }

            parent[rootB] = rootA;
            size[rootA] += size[rootB];
            maxi[rootA] = max(maxi[rootA], maxi[rootB]);
            mini[rootA] = min(mini[rootA], mini[rootB]);
            edges[rootA] += edges[rootB] + 1;
            components--;

            if (rank[rootA] == rank[rootB]) {
                rank[rootA]++;
            }
        }
        else {
            edges[rootA]++;
        }
        long long divers = (long long)edges[rootA]* (maxi[rootA] - mini[rootA]);
        cout << divers <<endl;
    }
};

int main() {
    int N, M;
    cin >> N >> M;

    DSU dsu(N);

    for (int i = 0; i < M; i++) {
        int a, b;
        cin >> a >> b;
        a--; b--;
        dsu.unionSets(a, b);
    }

    return 0;
}


