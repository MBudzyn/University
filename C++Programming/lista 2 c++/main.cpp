#include <iostream>
#include <cmath>
#include "kod.h"
#include "glowne.cpp"


using namespace std;



int main()
{


    punkt a(5,4);
    punkt b(11,3);
    punkt h(80,80);
    punkt g(20,13);
    punkt r(30,30);
    trojkat tr2(a,b,g);
    punkt c(100,0);
    punkt d(0,0);
    punkt e(0,100);
    trojkat tr(c,d,e);
    cout<<"czy trojkat o wsp ( (5,4) (9,3) (20,13) zawiera sie w trojkacie o wsp (100,0) (0,0) (0,100)): "<<tr.czyzawiera(tr2)<<endl; // "czy trojkat o wsp ( (5,4) (9,3) (20,13) zawiera sie w trojkacie o wsp (100,0) (0,0) (0,100))"
    cout<<"czy pkt (30,30) lezy w tr: "<<tr.czylezy(r)<<endl;
    cout<<"czy pkt (80,80) lezy w tr: "<<tr.czylezy(h)<<endl;
    cout<<"pole trojkata o wsp (0,100) (100,0) (0,0): "<<tr.pole()<<endl;
    cout<<"obwod trojkata o wsp (0,100) (100,0) (0,0): "<<tr.obwod()<<endl;
    tr.symetriasrodkowa(punkt(0,0));
    cout<<"wsp trojkat po przeksztalceniu przez symetrie srodkowa: ("<<tr.wsp_xjeden()<<" "<<tr.wsp_yjeden()<<") ("<<tr.wsp_xdwa()<<" "<<tr.wsp_ydwa()<<") ("<<tr.wsp_xtrzy()<<" "<<tr.wsp_ytrzy()<<")"<<endl;
    tr.symetriasrodkowa(punkt(0,0));
    wektor k(3,3);
    wektor kp(-3,-3);
    tr.przesun(k);
    cout<<"wsp trojkat po przesunieciu o  wektor (3,3): ("<<tr.wsp_xjeden()<<" "<<tr.wsp_yjeden()<<") ("<<tr.wsp_xdwa()<<" "<<tr.wsp_ydwa()<<") ("<<tr.wsp_xtrzy()<<" "<<tr.wsp_ytrzy()<<")"<<endl;
    tr.przesun(kp);
    odcinek w(punkt(0,0),punkt(4,4));
    w.symetriasrodkowa(punkt(0,0));
    cout<<"wspolrzedne koncow odcinka po wykonaniu symetrii srodkowej wzledem pkt (0,0): ("<<w.pierwszy.wsp_x()<<" "<<w.pierwszy.wsp_y()<<") ("<<w.drugi.wsp_x()<<" "<<w.drugi.wsp_y()<<")"<<endl;
    cout<<"czy pkt (-2,-2) nalezy do odcinka o koncach w pkt (0,0) (-4,-4): "<<w.czynalezy(punkt(-2,-2))<<endl;
    cout<<"czy pkt (0,0) nalezy do odcinka o koncach w pkt (0,0) (-4,-4): "<<w.czynalezy(punkt(0,0))<<endl;
    cout<<"czy pkt (0,3) nalezy do odcinka o koncach w pkt (0,0) (-4,-4): "<<w.czynalezy(punkt(0,3))<<endl;
    cout<<"dlugosc odcinka o koncach w pkt (0,0) (-4,-4): "<<w.dlugosc()<<endl;
    w.przesun(k);
    cout<<"wspolrzedne koncow odcinka po przesunieciu o wektor (3,3): ("<<w.pierwszy.wsp_x()<<" "<<w.pierwszy.wsp_y()<<") ("<<w.drugi.wsp_x()<<" "<<w.drugi.wsp_y()<<")"<<endl;
    a.przesun(k);
    cout<<"wsp pkt a: ("<<a.wsp_x()<<" "<<a.wsp_y()<<")"<<endl;
    a.przesun(k);
    cout<<"nowe wsp pkt a: ("<<a.wsp_x()<<" "<<a.wsp_y()<<")"<<endl;
    cout<<"wsp pkt b: ("<<b.wsp_x()<<" "<<b.wsp_y()<<")"<<endl;
    cout<<"odleglosc pkt a od b: "<<a.odleglosc(b)<<endl;
    a.symetriasrodkowa(b);
    cout<<"nowe wsp pkt a: ("<<a.wsp_x()<<" "<<a.wsp_y()<<")"<<endl;

    return 0;
}
