#pragma once
#include <iostream>
#include <string>
#include <vector>
using namespace std;
namespace gra {

    class Stangry {

        char zwyciezca;
        char rozmiar;
        char licznik;
        vector<string> elementy;
    public:
        void wyslwietl();
        Stangry(char rozmiar);
        bool czykoniec();
        void ruchgracza();
        void wstawX(char indeks);
        vector<string> zwroc();
        int zwrocrozmiar();
        void wyswietlzwyciezce();

    };
}

