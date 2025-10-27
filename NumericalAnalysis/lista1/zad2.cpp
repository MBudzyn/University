
#include <cmath>
using namespace std;

double funkcja(double argument)
{
    return 4046 * (sqrt(pow(argument,14) + 1) -1)/ pow(argument,14);
}
double funkcja2(double argument)
{
    return 4046 * 1/(sqrt(pow(argument,14)+1)+1);
}
void write_out_task_2()
{
    cout<<funkcja(0.001)<<endl;
    cout<<funkcja2(0.001)<<endl;
}
