#include <iostream>
#include <vector>
#include <iomanip>
#include <cmath>

using namespace std;

class Task {
private:
    int N;
    struct Point {
        long long x, y;
    };

    long long cross(const Point& a, const Point& b) {
        return a.x * b.y - a.y * b.x;
    }

    long double computePolygonArea(const vector<Point>& points) {
        long long area2 = 0;
        int n = points.size();
        for (int i = 0; i < n; ++i) {
            area2 += cross(points[i], points[(i + 1) % n]);
        }
        return static_cast<long double>(abs(area2)) / 2.0;
    }

public:
    void processData() {
        vector<Point> pnts;
        cin >> N;
        for (int i = 0; i < N; ++i) {
            Point p1;
            cin >> p1.x >> p1.y;
            pnts.push_back(p1);
        }

        long double area = computePolygonArea(pnts);
        area = floor(area * 10.0 + 0.5) / 10.0;

        cout << fixed << setprecision(1) << area << "\n";
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
