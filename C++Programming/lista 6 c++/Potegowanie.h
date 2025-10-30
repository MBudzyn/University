#pragma once

class Potegowanie: public Wyrazenie {
private:
    Wyrazenie *lewa;
    Wyrazenie *prawa;
public:
    double oblicz() override;
    string zapis() override;
    Potegowanie(Wyrazenie *jeden, Wyrazenie *dwa);

};
