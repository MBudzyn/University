// problem: we need to find the closest group of three points in a 2D plane
// we will use divide and conquer to solve this problem
// we will sort the points by x and y coordinates
#include <chrono>
#include<cmath>
#include <iostream>
#include <vector>
# include <algorithm>
#include <set>

using namespace std;

typedef pair<int, int> point;

vector<point> points;
vector<point> xList;
vector<point> yList;
vector<point*> yList2;

double distance(point a, point b){
    double sum = (a.first - b.first) * (a.first - b.first) +  (a.second - b.second) * (a.second - b.second);
    return sqrt(sum);
}

double perimeter(point a, point b, point c) {return distance(a, b) + distance(b, c) + distance(a, c);}

bool lessEqualBYX(point a, point b)
{
    if (a.first == b.first)
    {
        return a.second < b.second;
    }
    return a.first < b.first;
}
bool lessEqualBYY(point a, point b)
{
    if (a.second == b.second)
    {
        return a.first < b.first;
    }
    return a.second < b.second;
}

void prepareData(){
    xList = points;
    yList = points;

    sort(xList.begin(), xList.end(), lessEqualBYX);
    sort(yList.begin(), yList.end(), lessEqualBYY);
}

vector<point> bruteForce(vector<point> xTable)
{
    vector<point> result;
    double min = 1000000000;
    for (int i = 0; i < (int)xTable.size(); i++)
    {
        for (int j = i + 1; j < (int)xTable.size(); j++)
        {
            for (int k = j + 1; k < (int)xTable.size(); k++)
            {
                double p = perimeter(xTable[i], xTable[j], xTable[k]);
                if (p < min)
                {
                    min = p;
                    result.clear();
                    result.push_back(xTable[i]);
                    result.push_back(xTable[j]);
                    result.push_back(xTable[k]);

                }
            }
        }
    }
    return result;
}
int findCenterXLine(int start, int end)
{
    if ((start + end)% 2 == 1 )
    {
        int mid = (start + end) / 2;
        return (xList[mid].first + xList[mid - 1].first) / 2;
    }
    return xList[(start + end) / 2].first;
}


vector<point> get_fragment_x(int start, int end){
    vector<point> result;
    for(int i = start; i <= end; i++){
        result.push_back(xList[i]);
    }
    return result;
}
void loadData(){
    int n;
    cin>>n;
    for(int i = 0; i < n; i++){
        int x, y;
        cin>>x>>y;
        points.emplace_back(x, y);}

}
vector<point> createYInXRange2(double minX, double maxX)
{
    vector<point> result;
    //binary search
    int l = 0;
    int r = (int)xList.size() - 1;
    int mid;
    while (l <= r)
    {
        mid = (l + r) / 2;
        if (xList[mid].first >= minX && xList[mid].first <= maxX)
        {
            break;
        }
        if (xList[mid].first < minX)
        {
            l = mid + 1;
        }
        else
        {
            r = mid - 1;
        }
    }
    while (mid > 0 && xList[mid - 1].first >= minX)
    {
        mid--;
    }
    while (mid < (int)xList.size() && xList[mid].first <= maxX)
    {
        result.push_back(xList[mid]);
        mid++;
    }
    sort(result.begin(), result.end(), lessEqualBYY);
    return result;

}

vector<point> createYInXRange(double minX, double maxX)
{
    vector<point> result;
    for (auto & i : yList)
    {
        if (i.first >= minX && i.first <= maxX)
        {
            result.push_back(i);
        }
    }
    return result;
}


vector<point> createYInYRange(int start_index, double maxY, vector<point> yTable)
{
    vector<point> result;
    int i = start_index;
        while (i < (int)yTable.size() && yTable[i].second <= maxY)
        {
            result.push_back(yTable[i]);
            i++;
        }
    return result;
}

double minV = -1;
vector<point> finalResult;

void algo(int start_ind, int end_ind) {
    if (end_ind - start_ind < 6) {
        vector<point> pom1 = get_fragment_x(start_ind, end_ind);
        pom1 = bruteForce(pom1);
        double p = perimeter(pom1[0], pom1[1], pom1[2]);
        if (p < minV || minV == -1) {
            minV = p;
            finalResult = pom1;
        }
    }
    else{

        algo(start_ind,(end_ind+start_ind)/2);
        algo((end_ind + start_ind) /2 + 1, end_ind);
        double center = findCenterXLine(start_ind, end_ind);
        vector<point> Ylist = createYInXRange2(max((double)(center - minV / 2), (double)(xList[start_ind].first)),
                                              min((double)(center + minV / 2), (double)(xList[end_ind].first)));
        vector<point> temp;
        for (int i = 0; i < (int) Ylist.size(); i++) {
            temp = createYInYRange(i, Ylist[i].second + minV/2, Ylist);
            if (temp.size() < 3) {
                continue;
            }
            vector<point> pom_res = bruteForce(temp);
            double p = perimeter(pom_res[0], pom_res[1], pom_res[2]);
            if (p < minV) {
                minV = p;
                finalResult = pom_res;
            }
        }


    }
}

void execute(){
    //auto start = std::chrono::high_resolution_clock::now();
    algo(0,(int)xList.size()-1);
    vector<point> result = finalResult;
    cout<<result[0].first<<" "<<result[0].second<<endl;
    cout<<result[1].first<<" "<<result[1].second<<endl;
    cout<<result[2].first<<" "<<result[2].second;
//    auto end = std::chrono::high_resolution_clock::now();
//    std::chrono::duration<double, std::micro> czas_trwania = end - start;
//    std::cout << "Czas wykonania programu: " << czas_trwania.count() << " mikrosekund." << std::endl;


}

void brute(){
    auto start = std::chrono::high_resolution_clock::now();
    vector<point> result = bruteForce(xList);
    cout<<result[0].first<<" "<<result[0].second<<endl;
    cout<<result[1].first<<" "<<result[1].second<<endl;
    cout<<result[2].first<<" "<<result[2].second;
    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double, std::micro> czas_trwania = end - start;
    std::cout << "Czas wykonania programu: " << czas_trwania.count() << " mikrosekund." << std::endl;
}

int main() {
    loadData();
    prepareData();
//    for (int i= 0; i < (int)xList.size(); i++)
//    {
//        cout<<xList[i].first<<" "<<xList[i].second<<endl;
//    }
    execute();
   // brute();

    return 0;
}