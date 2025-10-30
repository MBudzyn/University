#pragma once

class Piksel {

protected:
    int x;
    int y;
    static const int maksxekran =  1920;
    static const int maksyekran = 1080;

public:
    Piksel();
    Piksel(int x,int y);
    int odlegloscprawy();
    int odleglosclewy();
    int odlegloscgora();
    int odlegloscdol();
    int getx();
    int gety();


};

class Pikselkolorowy : public Piksel {

protected:
    Kolornt kolor;
public:
    Pikselkolorowy();
    void przesunovector(int xmove,int ymove);
};

int distance (Piksel *piksel1 , Piksel *piksel2);

