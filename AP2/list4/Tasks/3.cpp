#include <iostream>
#include <math.h>
#include <vector>
#include <algorithm>

using namespace std;

class Task {
public:
    int N;
    int Q;
    int l, r;
    int sqrtN;
    vector<int> data;
    vector<int> appearances = vector<int>(100001, 0);
    vector<vector<int>> queries;
    int Answer = 0;

    Task() {
        run();
    }

    void prepare() {
        if (queries.empty()) return;
        l = queries[0][0];
        r = queries[0][1];

        for (int i = l; i <= r; i++) {
            if (data[i] >= 100001 || data[i] < 0) continue;
            appearances[data[i]]++;
            if (appearances[data[i]] == data[i]) {
                Answer++;
            } else if (appearances[data[i]] == data[i] + 1) {
                Answer--;
            }
        }
    }

    void lToRightStep() {
        if (data[l] < 0 || data[l] >= 100001) {
            l++;
            return;
        }
        appearances[data[l]]--;
        if (appearances[data[l]] == data[l]) {
            Answer++;
        } else if (appearances[data[l]] == data[l] - 1) {
            Answer--;
        }
        l++;
        if (l >= N) l = N - 1;
    }

    void lToLeftStep() {
        l--;
        if (l < 0) return;
        if (data[l] < 0 || data[l] >= 100001) return;
        appearances[data[l]]++;
        if (appearances[data[l]] == data[l]) {
            Answer++;
        } else if (appearances[data[l]] == data[l] + 1) {
            Answer--;
        }
    }

    void rToRightStep() {
        r++;
        if (r >= N) return;
        if (data[r] < 0 || data[r] >= 100001) return;
        appearances[data[r]]++;
        if (appearances[data[r]] == data[r]) {
            Answer++;
        } else if (appearances[data[r]] == data[r] + 1) {
            Answer--;
        }
    }

    void rToLeftStep() {
        if (data[r] < 0 || data[r] >= 100001){
            r--;
            return;
        }
        appearances[data[r]]--;
        if (appearances[data[r]] == data[r]) {
            Answer++;
        } else if (appearances[data[r]] == data[r] - 1) {
            Answer--;
        }
        r--;
        if (r < 0) r = 0;
    }

    void processQuestion(int start, int end) {
        while (l < start) {
            lToRightStep();
        }
        while (l > start) {

            lToLeftStep();
        }
        while (r < end) {
            rToRightStep();
        }
        while (r > end) {
            rToLeftStep();
        }
    }

    void loadData() {
        cin >> N >> Q;
        int tmp, a, b;
        data.resize(N);
        for (int i = 0; i < N; i++) {
            cin >> tmp;
            data[i] = tmp;
        }
        for (int i = 0; i < Q; i++) {
            cin >> a >> b;
            a--; b--;
            queries.push_back({a, b, i, 0});
        }
        sqrtN = floor(sqrt(N));
    }

    void answerQuestions() {
        for (vector<int>& q : queries) {
            processQuestion(q[0], q[1]);
            q[3] = Answer;
        }
    }

    bool compare(vector<int> a, vector<int> b) {
        if (a[0] / sqrtN != b[0] / sqrtN) {
            return a[0] / sqrtN < b[0] / sqrtN;
        }
        return a[1] < b[1];
    }

    void sortQueries() {
        sort(queries.begin(), queries.end(), [this](vector<int> a, vector<int> b) {
            return compare(a, b);
        });
    }

    void sortBack(vector<vector<int>>& queries) {
        sort(queries.begin(), queries.end(), Task::compareIndex);
    }

    static bool compareIndex(vector<int> a, vector<int> b) {
        return a[2] < b[2];
    }

    void run() {
        loadData();
        sortQueries();
        prepare();
        answerQuestions();
        sortBack(queries);
        for (vector<int>& q : queries) {
            cout << q[3] << endl;
        }
    }
};

int main() {
    Task task;
    return 0;
}
