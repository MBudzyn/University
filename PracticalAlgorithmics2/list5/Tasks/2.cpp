#include <iostream>
#include <math.h>
#include <vector>
#include <algorithm>

using namespace std;

class Struct{
public:
    vector<int> data;
    vector<pair<int, int>> structure;
    int range;

    Struct(vector<int> data){
        this->data = data;
    }
    void buildStructure(int l, int r){
        int tmp = 1000000002;
        this->range = r;
        for (int i = r; i >= 0; i--) {
            if (data[i] < tmp) {
                tmp = data[i];
                structure.insert(structure.begin(), {tmp, i});
            } else {
                structure.begin()->second = i;
            }
        }
    }
    static bool comparePair(pair<int, int> a, pair<int, int> b){
        return a.second < b.second;
    }
    int findAnswer(int l) {
        pair<int, int> res;

        auto it = lower_bound(structure.begin(), structure.end(),
                              make_pair(0, l), Struct::comparePair);
        if (it != structure.end() && it->second == l) {
            res = *it;
        } else if (it != structure.begin()) {
            --it;
            res = *it;
        } else {
            res = *it;
        }

        return res.first;
    }

    void increaseRange(){range++;}

    int answerQuestion(int l, int r){
        while (range <= r) {
            chooseCase(range, data[range]);
            increaseRange();
        }
        return findAnswer(l);
    }

    void chooseCase(int index, int value){
        if (structure.size() == 0) {
            structure.push_back({value, index});
        }
        else if (value < structure.back().first) {
            lessCase(value);
        } else if (value > structure.back().first) {
            greaterCase(index, value);
        }
    }

    void lessCase(int value){
        int new_index = structure.back().second;
        structure.pop_back();
        chooseCase(new_index, value);
    }

    void greaterCase(int index, int value){
        structure.push_back({value, index});
    }



};
class Task {

public:
    int N;
    int Q;
    Struct structure = Struct(vector<int>());
    vector<vector<int>> questions;
    vector<int> data;
    vector<int> answers;

    Task() {
        run();
    }

    void run() {
        loadData();
        prepare();
        answerQuestions();
    }

    static bool compare(vector<int> a, vector<int> b){
        return a[1] < b[1];
    }

    void answerQuestions(){
        for (vector<int> q : questions) {
            answers[q[2]] = structure.answerQuestion(q[0], q[1]);
        }
        for (int i = 0; i < Q; i++) {
            cout << answers[i] << endl;
        }
    }

    void prepare() {
        sort(questions.begin(), questions.end(), Task::compare);
        structure = Struct(data);
        structure.buildStructure(questions[0][0], questions[0][1]);
    }

    void loadData(){
        cin>>N>>Q;
        answers.resize(Q);
        int tmp;

        for (int i = 0; i < N; i++) {
            cin >> tmp;
            data.push_back(tmp);
        }

        for (int i = 0; i < Q; i++) {
            int a, b;
            cin >> a >> b;
            a--; b--;
            questions.push_back({a, b, i});
        }
    }
};

int main() {
    Task task;

    return 0;
}
