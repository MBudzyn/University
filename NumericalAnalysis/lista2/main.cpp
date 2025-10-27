#include <iostream>
#include "zad1.cpp"
using namespace std;
int main() {

    double i = 3.9999;
    while (i < 4.0001)
    {
        cout<<i<<" : "<<fun1(i)<<endl;
        i+= 0.000001;
    }
    c_better(1);

}
