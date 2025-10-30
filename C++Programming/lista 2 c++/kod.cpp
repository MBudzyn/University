#include <iostream>
#include <cmath>
#include "kod.h"

using namespace std;


bool trojkat :: czyzawiera(trojkat a) {
    if (czylezy(punkt(a.wsp_xjeden(),a.wsp_yjeden())) and czylezy(punkt(a.wsp_xdwa(),a.wsp_ydwa())) and czylezy(punkt(a.wsp_xtrzy(),a.wsp_ytrzy()))  )
        return true;
    else
        return false;
}

bool czyprostopadle(odcinek a,odcinek b)
{
    double dx1,dx2,dy1,dy2,a1,a2;
    dx1 = a.pierwszy.wsp_x()- a.drugi.wsp_x();
    dy1 = a.pierwszy.wsp_y() - a.drugi.wsp_y();
    dx2 = b.pierwszy.wsp_x()- b.drugi.wsp_x();
    dy2 = b.pierwszy.wsp_y() - b.drugi.wsp_y();
    if ( (dx1 == dy2 ) and dy2== 0)
        return true;
    if ( (dx2 == dy1 ) and dy1== 0)
        return true;

    return (dy1/dx1 * dy2/dx2 == -1);

}
bool czyrownolegle(odcinek a,odcinek b)
{
    double dx1,dx2,dy1,dy2;
    dx1 = a.pierwszy.wsp_x()- a.drugi.wsp_x();
    dy1 = a.pierwszy.wsp_y() - a.drugi.wsp_y();
    dx2 = b.pierwszy.wsp_x()- b.drugi.wsp_x();
    dy2 = b.pierwszy.wsp_y() - b.drugi.wsp_y();
    if ( dx1 == dx2 and dx1 == 0)
        return true;
    return (dy1/dx1 == dy2/dx2);
}

trojkat ::trojkat(punkt a, punkt b, punkt c) {
    odcinek o1(a,b);
    odcinek o2(a,c);
    odcinek o3(b,c);
    if (czyrownolegle(o1,o2 ) and czyrownolegle(o1,o3) and czyrownolegle(o2,o3))
    {
        clog<<"trojkat to nie prosta ani punkt"<<endl;
    }
    else
    {
        jeden=a;
        dwa=b;
        trzy=c;
    }

}
void trojkat ::symetriasrodkowa(punkt a) {jeden.symetriasrodkowa(a),trzy.symetriasrodkowa(a),dwa.symetriasrodkowa(a);}
trojkat ::trojkat(const trojkat &a) {this->jeden = a.jeden,this->dwa = a.dwa,this->trzy = a.trzy;}
void trojkat ::przesun(wektor t) {jeden.przesun(t),dwa.przesun(t),trzy.przesun(t);}
double trojkat ::wsp_xdwa() {return dwa.wsp_x();}
double trojkat ::wsp_xtrzy() {return trzy.wsp_x();}
double trojkat ::wsp_xjeden() {return jeden.wsp_x();}
double trojkat ::wsp_ydwa() {return dwa.wsp_y();}
double trojkat ::wsp_ytrzy() {return trzy.wsp_y();}
double trojkat ::wsp_yjeden() {return jeden.wsp_y();}


double trojkat ::pole() {
    double dl1,dl2,dl3;
    odcinek o1(jeden,dwa);
    odcinek o2(jeden,trzy);
    odcinek o3(dwa,trzy);
    dl1 = o1.dlugosc();
    dl2 = o2.dlugosc();
    dl3 = o3.dlugosc();
    double p = (dl3 + dl2 + dl1)/2;
    double wynik = sqrt(p*(p-dl2)*(p-dl1)*(p-dl3));
    return wynik;
}
double trojkat ::obwod() {
    double dl1,dl2,dl3;
    odcinek o1(jeden,dwa);
    odcinek o2(jeden,trzy);
    odcinek o3(dwa,trzy);
    dl1 = o1.dlugosc();
    dl2 = o2.dlugosc();
    dl3 = o3.dlugosc();
    return dl1 + dl2 + dl3;
}
bool trojkat ::czylezy(punkt a) {
    trojkat tr1 =trojkat(jeden,dwa,a);
    trojkat tr2 =trojkat(jeden,trzy,a);
    trojkat tr3 =trojkat(trzy,dwa,a);

    if( abs(this->pole() - (tr1.pole() + tr2.pole() + tr3.pole())) < 0.001)
        return true;
    else
        return false;

}

wektor :: wektor(double a,double  b){x=a,y=b;}
double wektor ::get_x() {return x;}
double wektor ::get_y() { return y;}
prosta :: prosta(double k, double z){a=k,b=z;}
double prosta::get_a() {return a;}
double prosta::get_b() {return b;}
punkt :: punkt(double a,double b){x=a,y=b;}
punkt ::punkt(const punkt &a) {this->x = a.x,this->y = a.y;}
double punkt::wsp_x () { return x; }
double punkt::wsp_y () { return y; }
void punkt ::przesun(wektor t) {x+=t.get_x(),y+=t.get_y();}
double punkt::odleglosc (punkt &p) {
    double dx=x-p.x, dy=y-p.y;
    return sqrt(dx*dx+dy*dy);
}
void punkt:: symetriasrodkowa(punkt a)
{wektor k(a.wsp_x()-x,a.wsp_y()-y);
 wektor c(2*k.get_x(),2*k.get_y());
 this->przesun(c);

}
void odcinek ::symetriasrodkowa(punkt a) {
    pierwszy.symetriasrodkowa(a);
    drugi.symetriasrodkowa(a);

}
odcinek :: odcinek(punkt a, punkt b) {
    if (a.wsp_x() == b.wsp_x() and a.wsp_y() == b.wsp_y())
        clog << "nie mozna utworzyc odcinka o dlugosci 0" << endl;
    else {
         pierwszy = a, drugi = b;
         }
}
odcinek ::odcinek(const odcinek &a) {this->pierwszy=a.pierwszy, this->drugi = a.drugi;}
void odcinek ::przesun(wektor t) {pierwszy.przesun(t),drugi.przesun(t);}
double odcinek ::dlugosc() {return pierwszy.odleglosc(drugi);}
bool odcinek ::czynalezy(punkt pkt) {


    double dx,dy,a,b;
    dx = pierwszy.wsp_x()- drugi.wsp_x();
    dy = pierwszy.wsp_y() - drugi.wsp_y();
    if (dx == 0)
    {
        if (pierwszy.wsp_x() == pkt.wsp_x() and pkt.wsp_y()<=pierwszy.wsp_y() and pkt.wsp_y()>= drugi.wsp_y())
            return true;
        if (pierwszy.wsp_x() == pkt.wsp_x() and pkt.wsp_y()>=pierwszy.wsp_y() and pkt.wsp_y()<= drugi.wsp_y())
            return true;
    }
    if ( dy == 0)
    {
        if (pierwszy.wsp_y() == pkt.wsp_y() and pkt.wsp_x()<=pierwszy.wsp_x() and pkt.wsp_x()>= drugi.wsp_x())
            return true;
        if (pierwszy.wsp_x() == pkt.wsp_x() and pkt.wsp_y()>=pierwszy.wsp_x() and pkt.wsp_x()<= drugi.wsp_x())
            return true;
    }
    a = dy/dx;
    b = pierwszy.wsp_y() - a * pierwszy.wsp_x();
    return (pkt.wsp_y()== a * pkt.wsp_x() + b);



}