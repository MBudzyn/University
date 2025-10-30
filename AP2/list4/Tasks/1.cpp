#include <iostream>
#include <math.h>
#include <vector>
using namespace std;

class Task1 {
public:
    int N;
    int Q;
    int sqrtN;
    vector<long long> data;
    vector<long long> sums;

    Task1() {
        loadData();
        preprocess();
        run();
    }
    void loadData() {
        long long x;
        cin>>N>>Q;
        sqrtN = ceil(sqrt(N));
        for (int i = 0; i < N; i++) {
            cin>>x;
            data.push_back(x);
        }
    }
    void preprocess() {
        for (int i = 0; i < N; i++) {
            if (i % sqrtN == 0) {
                sums.push_back(data[i]);
            } else {
                sums.back() += data[i];
            }
        }
    }
    void executeQuestion1(int positionK, int newValueU) {
        positionK -= 1;
        int block = positionK / sqrtN;
        sums[block] -= data[positionK];
        data[positionK] = newValueU;
        sums[block] += newValueU;
    }
    void executeQuestion2(int left, int right) {
        long long sum = 0;
        left -= 1;
        right -= 1;

        int startBlock = left / sqrtN;
        int endBlock = right / sqrtN;

        if (startBlock == endBlock) {
            for (int i = left; i <= right; i++) {
                sum += (long long)data[i];
            }
        } else {
            for (int i = left; i < (startBlock + 1) * sqrtN; i++) {
                sum += (long long)data[i];
            }
            for (int i = startBlock + 1; i < endBlock; i++) {
                sum += (long long)sums[i];
            }
            for (int i = endBlock * sqrtN; i <= right; i++) {
                sum += (long long)data[i];
            }
        }

        cout << sum << endl;
    }
    void executeQuestion(){
        int type, x, y;
        cin >> type >> x >> y;
        if (type == 1) {
            executeQuestion1(x, y);
        } else {
            executeQuestion2(x, y);
        }
    }
    void run(){
        for (int i = 0; i < Q; i++) {
            executeQuestion();
        }
    }
};

int main() {
    Task1 task1;

    return 0;
}


