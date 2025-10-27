#include <cmath>
using namespace std;

double fun_ex_5(int n)
{
    if (n == 0) {return ::log((double)2024/2023);}
    else return (double)1/n - (double)2023 * fun_ex_5(n-1);
}

void write_out_task_5()
{
    for (int i=0;i<21;i=i+2)
    {
        cout<<fun_ex_5(i)<<endl;
    }
    cout<<endl;
    for (int i=1;i<22;i=i+2)
    {
        cout<<fun_ex_5(i)<<endl;
    }
}