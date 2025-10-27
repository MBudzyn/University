#include <cmath>
using namespace std;


double fun_ex_4(double argument)
{
    if (argument == 0) {return 1;}
    if (argument == 1) {return (double)-1/9;}
    else return fun_ex_4(argument-1) * double(80)/9 + fun_ex_4(argument - 2);
}
double fun_ex_4_2(double n)
{
    return pow(double(-1)/9,n);
}
void write_out_task_4()
{
    for (int i=0;i<50;i++)
    {
        cout<<fun_ex_4_2(i)<<endl;
    }
}