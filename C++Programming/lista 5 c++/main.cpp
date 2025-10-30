using namespace std;
#include <iostream>
#include "kolor.h"
#include "Piksel.h"
#include<math.h>


int main() {



    try{
        Kolor czerwony = Kolor(255, 0, 0);
        cout <<"wartosc R koloru czerwonego " <<czerwony.getR() << endl;
        czerwony.przyciemnij(20);
        cout <<"aktualna wartosc R koloru czerwonego "<< czerwony.getR() << endl;
    }
    catch(invalid_argument e)
    {
        clog<<e.what()<<endl;
    }
    try{
        Pikselkolorowy nowy = Pikselkolorowy();
        Piksel nowy2 = Piksel();
        nowy.przesunovector(34, 56);
        nowy.getx();
        nowy.przesunovector(10, 34);
        cout<<"wsp x nowy: "<<nowy.getx()<<endl;
        cout<<"wsp y nowy: "<<nowy.gety()<<endl;
        nowy.odlegloscgora();
        nowy.odlegloscdol();
        nowy.odleglosclewy();
        nowy.odlegloscprawy();
        cout<<"odleglosc pikseli "<<distance(&nowy,&nowy2)<<endl;

    }
    catch(invalid_argument e)
    {
        clog<<e.what()<<endl;
    }

    try{
        Kolornazwany niebieski = Kolornazwany("Koniczyna");
    }
    catch(invalid_argument e)
    {
        clog<<e.what()<<endl;
    }
    try{
       Kolor nowy3 = Kolor();
       Kolor nowy4 = Kolornazwany("bialy");
       Kolor nowy5 = Kolorprzezroczysty(45);
       Kolor nowy6 = Kolornt();
       Kolor nowy7 = Kolor(34,120,70);
       nowy7.rozjasnij(40);
       nowy7.wypiszwszystkie();
       nowy7.przyciemnij(40);
       nowy7.wypiszwszystkie();
       nowy7.setR(50);
       nowy7.setG(50);
       nowy7.setB(50);
       nowy7.wypiszwszystkie();
       nowy6.wypiszwszystkie();
       nowy6.setG(76);
       nowy6.wypiszwszystkie();



    }
    catch(invalid_argument e)
    {
        clog<<e.what()<<endl;
    }


}





