#pragma once
#include <iostream>
#include <vector>
#include <string>
using namespace std;


class Zmienna final : public Wyrazenie {
private:
     static vector<pair<string, double>> tablica;
     string obecna;

public:
    void dodaj(pair<string, double> element);
    void zmienwartosc(string nazwa, double nowa);
    void usun(string nazwa);
    double oblicz() override;
    string zapis() override;
    Zmienna(string nazwa);
    void wypisztab();
    double zwrocwart(string nazwa);



};

