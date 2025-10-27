#include "komunikacja.h"
#include "Stangry.h"
#include "sztuczny.h"
using namespace std;
using namespace gra;


namespace komunikacja {
    void final() {

        srand(time(NULL));
        string wybor;
        string wybor2;
        Stangry p3 = Stangry(3);
        Stangry p4 = Stangry(4);
        cout << "wybierz 3 aby grac na planszy 3x3 albo 4 aby grac na planszy 4x4" << endl;
        cin >> wybor;
        cout << "wybierz 1 aby zaczynac 2 aby to komputer zaczynal" << endl;
        cin >> wybor2;
        if (wybor == "3" and wybor2 == "1") {
            while (!p3.czykoniec()) {
                p3.wyslwietl();
                p3.ruchgracza();
                if (p3.czykoniec()) break;
                p3.wstawX(sztuczny::sztuczna(p3.zwroc(), p3.zwrocrozmiar()));

            }
            p3.wyslwietl();
            p3.wyswietlzwyciezce();
        } else if (wybor == "4" and wybor2 == "1") {
            while (!p4.czykoniec()) {
                p4.wyslwietl();
                p4.ruchgracza();
                if (p4.czykoniec()) break;
                p4.wstawX(sztuczny::sztuczna(p4.zwroc(), p4.zwrocrozmiar()));

            }
            p4.wyslwietl();
            p4.wyswietlzwyciezce();
        } else if (wybor == "3" and wybor2 == "2") {
            while (!p3.czykoniec()) {
                p3.wstawX(sztuczny::sztuczna(p3.zwroc(), p3.zwrocrozmiar()));
                if (p3.czykoniec()) break;
                p3.wyslwietl();
                p3.ruchgracza();
            }
            p3.wyslwietl();
            p3.wyswietlzwyciezce();
        } else if (wybor == "4" and wybor2 == "2") {
            while (!p4.czykoniec()) {
                p4.wstawX(sztuczny::sztuczna(p4.zwroc(), p4.zwrocrozmiar()));
                if (p4.czykoniec()) break;
                p4.wyslwietl();
                p4.ruchgracza();
            }
            p4.wyslwietl();
            p4.wyswietlzwyciezce();
        } else cout << "nie wybrales poprawnej opcji" << endl;
    }
}