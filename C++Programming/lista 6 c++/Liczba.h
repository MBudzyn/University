#pragma once
#include <iostream>
#include <vector>
#include <string>
#include <math.h>
using namespace std;

class Liczba final : public Wyrazenie {
private:
    double liczba;
public:
    Liczba(double wartosc);
    double oblicz() override;
    string zapis() override;

};

