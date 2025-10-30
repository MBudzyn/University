#pragma once

class Ln: public Wyrazenie {
private:
    Wyrazenie *srodek;
public:
    double oblicz() override;
    string zapis() override;
    Ln(Wyrazenie *jeden);

};
