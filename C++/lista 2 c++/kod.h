using namespace std;

#ifndef LISTA_2_C___MAIN_H
#define LISTA_2_C___MAIN_H

class wektor{
private:
    double x,y;
public:
    wektor(double a, double b);
    double get_x();
    double get_y();


};
class prosta{
private:
    double a,b;
public:
    prosta(double a, double b);
    double get_a();
    double get_b();

};

class punkt {
protected:
    double x, y;
public:
    punkt (double a, double b);
    punkt (const punkt& a);
   // ~punkt ();
    void przesun(wektor t);
    double wsp_x ();
    double wsp_y ();
    double odleglosc (punkt &p);
    void symetriasrodkowa(punkt a);
};

class trojkat {

private:
    punkt jeden = punkt(0,0);
    punkt dwa = punkt(0,1) ;
    punkt trzy = punkt(1,0);
public:
    trojkat(punkt a,punkt b,punkt c);
    trojkat(const trojkat& a);
    void przesun(wektor t);
    double pole();
    double obwod();
    bool czylezy(punkt a);
    void symetriasrodkowa(punkt a);
    double wsp_xjeden();
    double wsp_yjeden ();
    double wsp_xdwa ();
    double wsp_ydwa ();
    double wsp_xtrzy ();
    double wsp_ytrzy ();
    bool czyzawiera(trojkat a);



};



class odcinek {
public:
    punkt pierwszy = punkt(0,0);
    punkt drugi = punkt(0,1);

    odcinek( punkt a, punkt b);
    odcinek(const odcinek& a);
    void przesun(wektor t);
    double dlugosc();
    bool czynalezy(punkt a);
    void symetriasrodkowa(punkt a);
};


#endif //LISTA_2_C___MAIN_H
