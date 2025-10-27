#include <iostream>
#include "Wyjdziel0.h"
#include "WyjWym.h"
#include "Wymierna.h"
#include "Wyjprzekzak.h"
using namespace std;



int main() {
    try {
        obliczenia::Wymierna z10 = obliczenia::Wymierna(23523450,999003);
        obliczenia::Wymierna z11 = obliczenia::Wymierna(2359348,999001);
        obliczenia::Wymierna z2 = z10 * z11;

        /*
       auto z1 = obliczenia::Wymierna(3);
       cout<<"stworzenie obiektu wymierna (z1) za pomoca konstruktora jednoargumentowego: "<<z1<<endl;
       obliczenia::Wymierna z2 = obliczenia::Wymierna(8,9);
       obliczenia::Wymierna z10 = obliczenia::Wymierna(2359348,99900);
       cout<<"stworzenie obiektu wymierna (z2) za pomoca konstruktora dwuargumentowego: "<<z2<<endl;
       obliczenia::Wymierna z3 = obliczenia::Wymierna();
       cout<<"stworzenie obiektu wymierna (z3) za pomoca konstruktora bezargumentowego: "<<z3<<endl;
       obliczenia::Wymierna z4 = z1 + z2;
       cout<<"stworzenie obiektu wymierna (z4) bedacego suma z1 (3,1) i z2 (8,9): "<<z4<<endl;
       obliczenia::Wymierna z5 = z3 - z2;
       cout<<"stworzenie obiektu wymierna (z5) bedacego roznica z3 (0,1) i z2 (8,9) : "<<z5<<endl;
       obliczenia::Wymierna z6 = z3 * z2;
       cout<<"stworzenie obiektu wymierna (z6) bedacego iloczynem z3 (0,1) i z2 (8,9) : "<<z6<<endl;
       obliczenia::Wymierna z7 = z2 / z1;
       cout<<"stworzenie obiektu wymierna (z7) bedacego ilorazem z2 (8,9) i z1 (3,1) : "<<z7<<endl;
       obliczenia::Wymierna z8 = !z2;
       cout<<"stworzenie obiektu wymierna (z8) bedacego odwrotnoscia z2 (8,9) : "<<z8<<endl;
       obliczenia::Wymierna z9 = -z2;
       cout<<"stworzenie obiektu wymierna (z9) bedacego przeciwna do z2 (8,9) : "<<z9<<endl;
       cout<<"rzutowanie obiektu z2 (8,9) na zmienna typu int: "<<int(z2)<<endl;
       cout<<"rzutowanie obiektu z2 (8,9) na zmienna typu double: "<<double(z2)<<endl;
       cout<<"licznik z5: "<<z5.getlicznik()<<" mianownik z5: "<<z5.getmianownik()<<endl;
       cout<<"stworzenie obiektu wymierna (z2) za pomoca konstruktora dwuargumentowego: "<<z10<<endl;
        */


    } catch(const std::exception& e) {
        cerr << "Exception: " << e.what() << endl;
    }

    return 0;
}
