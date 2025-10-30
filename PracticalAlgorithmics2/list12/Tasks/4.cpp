#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Task {
private:
    struct Point {
        long long x, y;

        bool operator<(const Point& other) const {
            return x < other.x || (x == other.x && y < other.y);
        }
    };

    int N;
    vector<Point> points;
    vector<Point> convex_hull;

    static long long cross(const Point& a, const Point& b, const Point& c) {
        return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x);
    }
public:
    void loadData() {
        cin >> N;
        points.resize(N);
        for (int i = 0; i < N; ++i) {
            cin >> points[i].x >> points[i].y;
        }
    }

    void execute() {
        sort(points.begin(), points.end());
        vector<Point> lower, upper;

        for (const auto& p : points) {
            while ((int)lower.size() >= 2 &&
                   cross(lower[lower.size() - 2], lower[lower.size() - 1], p) < 0) {
                lower.pop_back();
            }
            lower.push_back(p);
        }

        for (int i = N - 1; i >= 0; --i) {
            Point p = points[i];
            while ((int)upper.size() >= 2 &&
                   cross(upper[upper.size() - 2], upper[upper.size() - 1], p) < 0) {
                upper.pop_back();
            }
            upper.push_back(p);
        }

        convex_hull = lower;
        for (int i = 1; i + 1 < (int)upper.size(); ++i) {
            convex_hull.push_back(upper[i]);
        }

        sort(convex_hull.begin(), convex_hull.end());
    }

    void printResult() {
        cout << (int)convex_hull.size() << "\n";
        for (const auto& p : convex_hull) {
            cout << p.x << " " << p.y << "\n";
        }
    }

    void run() {
        loadData();
        execute();
        printResult();
    }
};

int main() {
    Task task;
    task.run();
    return 0;
}
