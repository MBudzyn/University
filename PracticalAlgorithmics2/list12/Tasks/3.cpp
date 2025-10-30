#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

class Task {
private:
    int N;

    struct Point {
        long long x, y;
    };

    long double pointToLineDistance(const Point& p1, const Point& p2, const Point& q) {
        long long dx = p2.x - p1.x;
        long long dy = p2.y - p1.y;
        long long num = abs(dx * (p1.y - q.y) - (p1.x - q.x) * dy);
        long double den = sqrtl(dx * dx + dy * dy);
        return num / den;
    }

public:
    void processData() {
        cin >> N;
        for (int i = 0; i < N; ++i) {
            Point p1, p2, q;
            cin >> p1.x >> p1.y >> p2.x >> p2.y >> q.x >> q.y;
            long double dist = pointToLineDistance(p1, p2, q);
            cout << fixed << setprecision(10) << dist << "\n";
        }
    }

    void run() {
        processData();
    }
};

int main() {

    Task task;
    task.run();
    return 0;
}
