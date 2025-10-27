#include<string>
#pragma once

class Kolor {

protected:
    unsigned char R;
    unsigned char G;
    unsigned char B;
public:

    Kolor(int r, int g, int b);
    Kolor();
    void setR(int r);
    int getR();
    void setG(int g);
    int getG();
    void setB(int b);
    int getB();
    void rozjasnij(int procent);
    void przyciemnij(int procent);
    void wypiszwszystkie();

};

class Kolorprzezroczysty : public virtual Kolor
{
protected:
    int alfa;
public:
    Kolorprzezroczysty();
    Kolorprzezroczysty(int alfa);

};

class Kolornazwany : public virtual Kolor
{
protected:
    string nazwa;
public:
    Kolornazwany();
    Kolornazwany(string nazwa);

};

class Kolornt: public Kolornazwany, public Kolorprzezroczysty
{

};