# include <iostream>
# include <vector>
# include <algorithm>
using namespace std;

class Task {
public:
    int N;
    vector<vector<int>> data;
    vector<int> dp;

    Task() {

    }

    void loadData(){
        cin >> N;
        vector<vector<int>> tmpData;
        for (int i = 0; i < N; i++){
            vector<int> tmp;
            for (int j = 0; j < N; j++){
                int x;
                cin>>x;
                tmp.push_back(x);
            }
            tmpData.push_back(tmp);
        }
        this->data = tmpData;
        this->dp.resize(1<<N, -1);
    }

    static unsigned int nextCombination(unsigned int bitMask){
        unsigned int c = bitMask & -bitMask;
        unsigned int r = bitMask+ c;
        return (((r ^ bitMask) >> 2) / c) | r;
    }

    static int turnOffIthBit(int bitMask, int i){ return bitMask ^ (1<<i);}

    static bool isIthBitTurnOn(int bitMask, int i){ return (bitMask & (1<<i)) != 0;}

    static int getFirstIBitsTurnOn(int i){ return (1<<i) - 1;}

    static vector<int> getAllCombination(int length, int bitMask){
        vector<int> result;
        while (bitMask < (1<<length)) {
            result.push_back(bitMask);
            bitMask = nextCombination(bitMask);
        }
        return result;
    }

    void fillStartDP(){
        for (int machine_ind = 0; machine_ind < N; machine_ind++){
            dp[1<<machine_ind] = data[0][machine_ind];
        }
    }

    void solve(){
        fillStartDP();
        for (int worker_ind = 1; worker_ind< N; worker_ind++) {
            int start = getFirstIBitsTurnOn(worker_ind+1);
            vector<int> combinations = getAllCombination(N, start);
            for (int comb: combinations) {
                for (int machine_ind = 0; machine_ind < N; machine_ind++) {
                    if (isIthBitTurnOn(comb, machine_ind)) {
                        dp[comb] = max(dp[comb], dp[turnOffIthBit(comb, machine_ind)] +
                                                 data[worker_ind][machine_ind]);
                    }
                }
            }
        }
    }

    void printResult(){
        cout<<dp[(1<<N) - 1]<<endl;
    }

    void run(){
        loadData();
        solve();
        printResult();
    }
};

int main() {
    Task task = Task();
    task.run();

    return 0;
}
