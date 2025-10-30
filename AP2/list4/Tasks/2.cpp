#include <iostream>
#include <math.h>
#include <vector>
using namespace std;

class Task2 {
public:
    int N;
    int Q;
    int sqrtN;
    vector<long long> data;
    vector<vector<long long>> tmpData;

    Task2() {
        loadData();
        preprocess();
        run();
    }
    void loadData() {
        long long x;
        cin>>N;
        sqrtN = ceil(sqrt(N));
        for (int i = 0; i < N; i++) {
            cin>>x;
            data.push_back(x);
        }
        cin>>Q;
    }
    void preprocess() {
        for (int i = 0; i < sqrtN; i++) {
            vector<long long> tmp(N, 0);
            for (int j = N - 1; j >= 0; j-= 1 ){
                tmp[j] = data[j];
                if (j + i + 1< N) {
                    tmp[j] += tmp[j + i + 1];
                }
            }
            tmpData.push_back(tmp);
        }
    }

    void brute(int start, int jump){
        long long sum = 0;
        for (int i = start -1; i < N; i+=jump) {
            sum += data[i];
        }
        cout<<sum<<endl;
    }
    void answer(int left, int jump){
        long long sum = 0;
        if (jump >= sqrtN) {
            brute(left, jump);
            return;
        }
        cout<< tmpData[jump-1][left - 1]<<endl;
    }
    void run(){
        int left, jump;
        for (int i = 0; i < Q; i++) {
            cin>>left>>jump;
            answer(left, jump);
        }
    }

    void print() {
        for(vector<long long> v : tmpData) {
            for(long long x : v) {
                cout<<x<<" ";
            }
            cout<<endl;
        }
    }
};
int main() {
    Task2 task2;

    return 0;
}


