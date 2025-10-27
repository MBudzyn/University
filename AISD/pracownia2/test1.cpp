// problem: we need to find the closest group of three points in a 2D plane
// we will use divide and conquer to solve this problem
// we will sort the points by x and y coordinates

#include<cmath>
#include <iostream>
#include <vector>
# include <algorithm>
using namespace std;

typedef pair<int, int> point;

vector<point> points;
vector<point> xList;
vector<point> yList;

double distance(point a, point b){
    double sum = (a.first - b.first) * (a.first - b.first) +  (a.second - b.second) * (a.second - b.second);
    return sqrt(sum);
}

double perimeter(point a, point b, point c) {return distance(a, b) + distance(b, c) + distance(a, c);}

point middlePoint(point a, point b) {return point((a.first + b.first) / 2, (a.second + b.second) / 2);}

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
    for (int i = 0; i < xTable.size(); i++)
    {
        for (int j = i + 1; j < xTable.size(); j++)
        {
            for (int k = j + 1; k < xTable.size(); k++)
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


int findCenterXLine()
{
    if (xList.size() % 2 == 0)
    {
        return (xList[xList.size() / 2].first + xList[xList.size() / 2 - 1].first) / 2;
    }
    return xList[xList.size() / 2].first;

}
vector<point> firstHalf(vector<point> xTable)
{
    vector<point> result;
    for (int i = 0; i < xTable.size() / 2; i++)
    {
        result.push_back(xTable[i]);
    }
    return result;
}
vector<point> secondHalf(vector<point> xTable)
{
    vector<point> result;
    for (int i = xTable.size() / 2; i < xTable.size(); i++)
    {
        result.push_back(xTable[i]);
    }
    return result;
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
    for (int i = start_index; i < start_index + 16; i++)
    {
        if (i >= 0 && i < yTable.size() && yTable[i].second <= maxY)
        {
            result.push_back(yTable[i]);
        }
    }
    return result;
}


vector<point> algo(int start_ind, int end_ind, double centerLine){
    vector<point> result;
    if(end_ind - start_ind < 6)
    {
        result = bruteForce(get_fragment_x(start_ind, end_ind));
        double minV = perimeter(result[0], result[1], result[2]);
        vector<point> Ylist = createYInXRange(centerLine - minV/2, centerLine + minV/2);
        vector<point> temp;
        for (int i = 0; i < Ylist.size(); i++)
        {
            temp = createYInYRange(i, Ylist[i].second + minV/2, Ylist);
            if (temp.size() < 3)
            {
                continue;
            }
            vector<point> pom_res = bruteForce(temp);
            double p = perimeter(pom_res[0], pom_res[1], pom_res[2]);
            if (p < minV)
            {
                minV = p;
                result = pom_res;
            }
        }
        return result;
    }
    else{
        double center = findCenterXLine();
        vector<point> res1 = algo(start_ind,(end_ind+start_ind)/2, center);
        vector<point> res2 = algo((end_ind + start_ind) /2 + 1, end_ind, center);
        if (perimeter(res1[0], res1[1], res1[2]) < perimeter(res2[0], res2[1], res2[2]))
        {
            return res1;
        }
        return res2;
    }
}

void execute(){
    loadData();
    prepareData();
    vector<point> result = algo(0,xList.size() -1, findCenterXLine());
    cout<<result[0].first<<" "<<result[0].second<<endl;
    cout<<result[1].first<<" "<<result[1].second<<endl;
    cout<<result[2].first<<" "<<result[2].second;


}

int main() {
    execute();
    return 0;
}