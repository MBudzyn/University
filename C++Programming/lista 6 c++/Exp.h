#pragma once

class Exp: public Wyrazenie {
private:
    Wyrazenie *srodek;
public:
    double oblicz() override;
    string zapis() override;
    Exp(Wyrazenie *jeden);

};
