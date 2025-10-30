#include <bits/stdc++.h>
#include <iostream>
#include <vector>
using namespace std;

// pisanie w kilku linijkach clion skrót klawiszowy

string bin2rzym (int x)
{
   vector<pair<int, string>> rzym = {
        {1000, "M"},
        {900, "CM"},
        {500, "D"},
        {400, "CD"},
        {100, "C"},
        {90, "XC"},
        {50, "L"},
        {40, "XL"},
        {10, "X"},
        {9, "IX"},
        {5, "V"},
        {4, "IV"},
        {1, "I"}};
    string w ="";
    for(int i=0;i<13;i++)
    {
        int z = rzym[i].first;
        while(x>=z)
        {
            x = x-z;
            w = w+rzym[i].second;
        }
    }
    return w;

}


int main(int argc,char *argv[])
{

for(int i=1; i<argc; i++)
    {
        try
        {
            int z = stoi(argv[i]);
            if (z < 4000 && z > 0)
                cout << bin2rzym(z) << endl;
            else
                clog << argv[i] << "argument poza zakresem" << endl;
        }
        catch(...)
        {
            clog << argv[i] << " niepoprawny argument" << endl;
        }
    }
return 0;
}
