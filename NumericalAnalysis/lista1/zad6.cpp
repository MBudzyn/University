#include <cmath>
using namespace std;

double fun_ex_6(int n)
{
    double sum = 0;
    for (int i=0; i<n;i++)
        sum = sum + pow(-1,i)/(2 * i +1);
    return (double)4 * sum;
}

void write_out_task_6() {
    for (int i = 1999990; i < 2000002; i++) {
        cout << fun_ex_6(i) << endl;
    }
}
