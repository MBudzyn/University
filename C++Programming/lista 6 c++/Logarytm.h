#pragma once

class Logarytm: public Wyrazenie {
private:
    Wyrazenie *lewa;
    Wyrazenie *prawa;
public:
    double oblicz() override;
    string zapis() override;
    Logarytm(Wyrazenie *jeden, Wyrazenie *dwa);

};