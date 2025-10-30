#pragma once
#include <iostream>
#include <vector>
#include <string>
#include <math.h>
using namespace std;

class Pi final : public Wyrazenie {
private:
    const double pi = 3.1415;
public:
    double oblicz() override;
    string zapis() override;

};


