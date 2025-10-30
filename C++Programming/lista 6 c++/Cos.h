#pragma once

class Cos: public Wyrazenie {
private:
    Wyrazenie *srodek;
public:
    double oblicz();
    string zapis();
    Cos(Wyrazenie *jeden);

};
