
#include <cmath>
using namespace std;


double fun_ex_3(double argument)
{
    return (double)14 * ((double)1 - cos((double)17 * argument))/argument * argument;
}
float fun_ex_3_2(float argument)
{
    return 14.0f * (1.0f - cos(17.0f * argument))/argument * argument;
}
void write_out_task_3()
{
    for (int i=11;i<21;i++)
    {
        cout<<fun_ex_3(pow((double)10,-i))<<endl;
    }

    for (int i=11;i<21;i++)
    {
        cout<<fun_ex_3_2((float)pow(10.0f,-i))<<endl;
    }
}