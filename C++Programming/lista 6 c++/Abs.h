#pragma once

class Abs: public Wyrazenie {
private:
    Wyrazenie *srodek;
public:
    double oblicz();
    string zapis();
    Abs(Wyrazenie *jeden);

};
