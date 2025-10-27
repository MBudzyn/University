#include <iostream>
#include <vector>
using namespace std;

struct Coin {
    int value;
    int mass;
};

class Solution {
    int numCoins;
    int finalMass;
    vector<int> maxT;
    vector<int> minT;
    vector<int> maxIndex;
    vector<int> minIndex;
    vector<int> minResult;
    vector<int> maxResult;
    vector<Coin> coins;
    bool isPossible = false;

public:
    void loadData() {
        cin >> finalMass;
        cin >> numCoins;
        maxIndex.resize(finalMass + 1);
        minIndex.resize(finalMass + 1);
        maxT.resize(finalMass + 1);
        minT.resize(finalMass + 1);
        coins.resize(numCoins);
        maxResult.resize(numCoins);
        minResult.resize(numCoins);
        for (int i = 0; i <= finalMass; i++) {
            minT[i] = 1000000000;
        }

        for (int i = 0; i < numCoins; i++) {
            cin >> coins[i].value;
            cin >> coins[i].mass;

        }
    }

    void coin_equal_weight_case(int coin_index, int weight) {
        if (coins[coin_index].value > maxT[weight]) {
            maxT[weight] = coins[coin_index].value;
            maxIndex[weight] = coin_index;
        }
        if (coins[coin_index].value < minT[weight]) {
            minT[weight] = coins[coin_index].value;
            minIndex[weight] = coin_index;
        }
    }

    void coin_smaller_weight_case(int coin_index, int mass) {
        int index = mass - coins[coin_index].mass;
        if (maxT[index] != 0) {
            if (maxT[index] + coins[coin_index].value > maxT[mass]) {
                maxT[mass] = maxT[index] + coins[coin_index].value;
                maxIndex[mass] = coin_index;
            }
        }

        if (minT[index] != 0) {
            if (minT[index] + coins[coin_index].value < minT[mass]) {
                minT[mass] = minT[index] + coins[coin_index].value;
                minIndex[mass] = coin_index;
            }
        }
    }

    void solve() {
        for (int i = 0; i <= finalMass; i++) {
            for (int j = 0; j < numCoins; j++) {
                if (coins[j].mass <= i) {
                    if (coins[j].mass == i) {
                        coin_equal_weight_case(j, i);
                    } else {
                        coin_smaller_weight_case(j, i);
                    }
                }
            }
        }
    }

    void prepareOutput() {
        int max = maxT[finalMass];
        if (max != 0)
        {
            isPossible = true;
            int index = finalMass;
            while (index > 0)
            {
                maxResult[maxIndex[index]]++;
                index -= coins[maxIndex[index]].mass;
            }
            index = finalMass;
            while (index > 0)
            {
                minResult[minIndex[index]]++;
                index -= coins[minIndex[index]].mass;
            }
        }
    }

    void printOutput() {
        if (isPossible) {
            cout << "TAK" << endl;
            cout << minT[finalMass] << endl;
            for (int i = 0; i < numCoins; i++) {
                cout << minResult[i] << " ";
            }
            cout << endl;
            cout << maxT[finalMass] << endl;
            for (int i = 0; i < numCoins; i++) {
                cout << maxResult[i] << " ";
            }
        } else {
            cout << "NIE";
        }
    }
    void execute() {
        loadData();
        solve();
        prepareOutput();
        printOutput();
    }
};



int main() {
    Solution solution;
    solution.execute();



    return 0;
}
