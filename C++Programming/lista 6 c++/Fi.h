#pragma once
#include <iostream>
#include <vector>
#include <string>
#include <math.h>
using namespace std;

class Fi final : public Wyrazenie {
private:
    const double fi = 1.618;
public:
    double oblicz() override;
    string zapis() override;

};
