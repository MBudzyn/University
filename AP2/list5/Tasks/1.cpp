#include <iostream>
#include <math.h>
#include <vector>
#include <algorithm>

using namespace std;

class Task {

public:
    int N;
    int Q;
    vector<int> data;
    vector<vector<int>> preprocessedData;
    vector<pair<int, int>> questions;


    Task() {
        run();

    }

    void run(){
        loadData();
        prepare();
        answerAll();
    }

    void prepare() {
        int nSqrt = floor(sqrt(N));
        preprocessedData.resize(nSqrt + 1);
        preprocessedData[0] = data;
        for (int i = 1; i <= nSqrt; i++) {
            for (int j = 0; j < N - pow(2, i) + 1; j++) {
                preprocessedData[i].push_back(min(preprocessedData[i-1][j], preprocessedData[i-1][j + pow(2, i - 1)]));
            }
        }
    }

    void printPreprocessed(){
        for (int i = 0; i < preprocessedData.size(); i++) {
            for (int j = 0; j < preprocessedData[i].size(); j++) {
                cout<<preprocessedData[i][j]<<" ";
            }
            cout<<endl;
        }
    }

    void answer(int l, int r){
        if (l == r) {
            cout << data[l] << endl;
            return;
        }
        int length = r - l + 1;
        int k = floor(log2(length));
        if (length == pow(2, k)) {
            int start_pos = l;
            int second_pos = l + pow(2, k-1);
            cout << min(preprocessedData[k-1][start_pos], preprocessedData[k-1][second_pos]) << endl;
        }
        else {
            int start_pos = l;
            int second_pos = r - pow(2, k) + 1;
            cout << min(preprocessedData[k][start_pos], preprocessedData[k][second_pos]) << endl;
        }
    }

    void answerAll(){
        for (int i = 0; i < Q; i++) {
            answer(questions[i].first, questions[i].second);
        }
    }

    void loadData(){
        cin>>N>>Q;
        int tmp;

        for (int i = 0; i < N; i++) {
            cin >> tmp;
            data.push_back(tmp);
        }

        for (int i = 0; i < Q; i++) {
            int a, b;
            cin >> a >> b;
            a--; b--;
            questions.push_back({a, b});
        }
    }
};

int main() {
    Task t;
    return 0;
}
