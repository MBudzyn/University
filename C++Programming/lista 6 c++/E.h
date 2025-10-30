#pragma once
#include <iostream>
#include <vector>
#include <string>
#include <math.h>
using namespace std;

class E final : public Wyrazenie {
private:
    const double e = 2.73;
public:
    double oblicz() override;
    string zapis() override;
};
