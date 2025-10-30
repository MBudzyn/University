#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Task {
private:
    int N;
    struct Point {
        long long x, y;
    };

    long long crossProduct(Point a, Point b, Point c) {
        long long vx1 = b.x - a.x;
        long long vy1 = b.y - a.y;
        long long vx2 = c.x - a.x;
        long long vy2 = c.y - a.y;
        return vx1 * vy2 - vy1 * vx2;
    }

public:
    void processData(){
        cin >> N;
        for (int i = 0; i < N; ++i) {
            Point p1, p2, p3;
            cin >> p1.x >> p1.y >> p2.x >> p2.y >> p3.x >> p3.y;
            answer(p1, p2, p3);
        }
    }

    void answer(Point p1, Point p2, Point p3) {
        long long cross = crossProduct(p1, p2, p3);
        if (cross == 0) {
            cout<<"TOUCH"<<endl;
        } else if (cross > 0) {
            cout<<"LEFT"<<endl;
        } else {
            cout<<"RIGHT"<<endl;
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
