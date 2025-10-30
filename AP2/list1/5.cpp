#include <iostream>
#include <vector>
using namespace std;


class Queens
{
public:
    int actualPosition;
    int n;
    vector<int> board;
    int solutions;
    int valToSet;


    Queens(int n)
    {
        this->n = n;
        this->board = vector<int>(n, -1);
        this->actualPosition = 0;
        this->solutions = 0;
        this->valToSet = 0;
    }

    bool isValOutOfBounds() const {
        return valToSet >= n;
    }

    void stepBack() {
        board[actualPosition] = -1;
        actualPosition--;
        valToSet = board[actualPosition] + 1;
    }

    bool endCondition() const {
        return actualPosition == -1;
    }
    void setVal() {
        board[actualPosition] = valToSet;
        valToSet = 0;
        actualPosition++;
    }

    bool checkDiagonalBack() {
        int up = valToSet, down = valToSet;
        for (int i = actualPosition - 1; i >= 0; i--) {
            up++;
            down--;
            if (board[i] == down || board[i] == up) return false;
        }
        return true;
    }

    bool checkRow() {
        for (int i = actualPosition - 1; i >= 0; i--) {
            if (board[i] == valToSet) return false;
        }
        return true;
    }

    bool isFinal() const {
        return actualPosition == n;
    }

    bool check() {
        return checkDiagonalBack() && checkRow();
    }

    int solve() {
        while (!endCondition()) {
            if (isFinal()) {
                solutions++;
                actualPosition--;
                valToSet = board[actualPosition] + 1;
            } else if (isValOutOfBounds()) {
                stepBack();
            } else if (check()) {
                setVal();
            } else {
                valToSet++;
            }
        }
        return solutions;
    }

};

int main() {
    int n;
    cin >> n;
    Queens q(n);
    cout << q.solve() << endl;
}
