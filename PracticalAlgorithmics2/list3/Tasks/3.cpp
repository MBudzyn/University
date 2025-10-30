#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class DSU {
public:
    vector<int> parent, rank, size;
    int components;
    int maxSize;

    DSU(int n) {
        parent.resize(n);
        rank.resize(n, 0);
        size.resize(n, 1);
        components = n;
        maxSize = 1;
        for (int i = 0; i < n; i++) {
            parent[i] = i;
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
            maxSize = max(maxSize, size[rootA]);
            components--;

            if (rank[rootA] == rank[rootB]) {
                rank[rootA]++;
            }

        }
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
        cout << dsu.components << " " << dsu.maxSize << endl;
    }

    return 0;
}


