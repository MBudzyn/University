#include "klasa liczba.h"
#include <iostream>
int main()
{
    liczba u;
    u.wypiszktualna();
    u.nadajnowo(6);
    u.nadajnowo(3);
    u.wypiszktualna();
    cout<<endl;
    cout<<"testy t"<<endl;
    cout<<endl;
    liczba t(4); // aktualna = 4 historia = .....
    t.wypiszktualna();
    t.nadajnowo(5); // aktualna = 5 historia = 4
    t.nadajnowo(6); // aktualna = 6 historia = 5 4
    t.nadajnowo(283); // aktualna = 283 historia = 6 5
    t.wypiszktualna();
    t.ostatniahistoria(); // aktualna = 6 historia = 5
    liczba k(t);
    liczba h(5);
    t.wypiszktualna();
    t.ostatniahistoria(); // aktualna = 5 historia = ........
    t.wypiszktualna();
    t.nadajnowo(10); //aktualna = 10 historia = 5
    t.wypiszktualna();
    t.ostatniahistoria(); // aktualna = 5 historia = ........
    t.wypiszktualna();
    t.ostatniahistoria(); // aktualna = 5 historia = ........
    t.wypiszktualna();
    cout<<endl;
    cout<<"testy o przeniesionego z t"<<endl;
    cout<<endl;
    liczba o = move(h);
    o.wypiszktualna();
    o.nadajnowo(52);
    o.nadajnowo(34);
    o.nadajnowo(43);
    o.wypiszktualna();
    o.ostatniahistoria();
    o.wypiszktualna();
    o.ostatniahistoria();
    o.nadajnowo(1);
    o.wypiszktualna();
    o.nadajnowo(445242);
    o.wypiszktualna();
    o.ostatniahistoria();
    o.wypiszktualna();
    o.ostatniahistoria();
    o.nadajnowo(32532);
    o.wypiszktualna();
    liczba y =(o);
    cout<<endl;
    cout<<"testy y skopiowanego z o"<<endl;
    cout<<endl;
    y.wypiszktualna();
    y.nadajnowo(1);
    y.nadajnowo(2);
    y.nadajnowo(423);
    y.wypiszktualna();
    y.ostatniahistoria();
    y.wypiszktualna();
    y.ostatniahistoria();
    y.nadajnowo(4);
    y.wypiszktualna();
    y.nadajnowo(413);
    y.wypiszktualna();
    y.ostatniahistoria();
    y.wypiszktualna();
    y.ostatniahistoria();
    y.nadajnowo(9);
    y.wypiszktualna();



    return 0;
}