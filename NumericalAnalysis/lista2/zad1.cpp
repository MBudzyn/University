#include <math.h>
using namespace std;
double fun1(double x)
{
return log(x/4);
}

float c_better(float x){
    float sum = 0;
    if(abs(x) > 1)
        cout << (M_PI/2 - x - atan(1/x))/pow(x, 3) << endl;
    else {
        for(int i = 0; i < 10000; i++) {
            sum += pow(-1, i + 1) * pow(x, 2 * i) / (2 * i + 3);
        }
        cout << sum << endl;
    }
}
