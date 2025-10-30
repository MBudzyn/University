#pragma once

class Sin: public Wyrazenie {
private:
    Wyrazenie *srodek;
public:
    double oblicz() override;
    string zapis() override;
    Sin(Wyrazenie *jeden);

};

