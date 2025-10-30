#include "komunikacja.h"
#include "Stangry.h"
using namespace std;
using namespace gra;

namespace sztuczny {
    int sztuczna(vector<string> tablica , int rozmiar) {
        vector<int> zmienny = {};
        if (rozmiar == 4)
        {
            for (int i = 0; i < 16; i++) {
                if (tablica[i] == " ") { zmienny.push_back(i); }
            }
            int t = rand() % zmienny.size();
            return zmienny[t];
        }
        if (rozmiar == 3)
        {
            for (int i = 0; i < 9; i++) {
                if (tablica[i] == " ") { zmienny.push_back(i); }
            }
            int t = rand() % zmienny.size();
            return zmienny[t];
        }
    }
}
