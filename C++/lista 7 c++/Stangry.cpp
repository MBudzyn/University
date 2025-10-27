#include <stdexcept>
#include "Stangry.h"
#include <cctype>

namespace gra {
    Stangry::Stangry(char t)
    {
        licznik = 0;
        zwyciezca = 0;
        if (t != 3 and t != 4)
            throw invalid_argument("nie mozna  stworzyc pola o podanym rozmiarze");

        if ( t == 3)
        {
            elementy = {" ", " ", " ", " ", " ", " ", " ", " ", " "};
            rozmiar = 3;
        }
        if ( t == 4)
        {
            elementy = {" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "};
            rozmiar = 4;
            }
    }

    void Stangry::wyslwietl() {

        if  (rozmiar == 4) {
            cout << "---------------------" << endl;
            cout << "| # | A | B | C | D |" << endl;
            cout << "---------------------" << endl;
            cout << "| 1 | " << elementy[0] << " | " << elementy[1] << " | " << elementy[2] << " | " << elementy[3]<< " |" << endl;
            cout << "---------------------" << endl;
            cout << "| 2 | " << elementy[4] << " | " << elementy[5] << " | " << elementy[6] << " | " << elementy[7]<< " |" << endl;
            cout << "---------------------" << endl;
            cout << "| 3 | " << elementy[8] << " | " << elementy[9] << " | " << elementy[10] << " | " << elementy[11]<< " |" << endl;
            cout << "---------------------" << endl;
            cout << "| 4 | " << elementy[12] << " | " << elementy[13] << " | " << elementy[14] << " | " << elementy[15] << " |" << endl;
            cout << "---------------------" << endl;
        }

        if  (rozmiar == 3) {
            cout << "-----------------" << endl;
            cout << "| # | A | B | C |" << endl;
            cout << "-----------------" << endl;
            cout << "| 1 | " << elementy[0] << " | " << elementy[1] << " | " << elementy[2] << " | " << endl;
            cout << "-----------------" << endl;
            cout << "| 2 | " << elementy[3] << " | " << elementy[4] << " | " << elementy[5] << " | " << endl;
            cout << "-----------------" << endl;
            cout << "| 3 | " << elementy[6] << " | " << elementy[7] << " | " << elementy[8] << " | " << endl;

            cout << "-----------------" << endl;

        }
    }

    void Stangry::wstawX(char ind) { elementy[ind] = "X"; licznik++;}

    vector<string> Stangry::zwroc() { return elementy; }
    int Stangry::zwrocrozmiar() { return rozmiar; }

    void Stangry::ruchgracza() {
        char z1;
        char z2;
        short int pole;
        string zmienna;
        cout << "wybierz pole na ktorym chcesz postawic kolo najpierw podaj Litere potem cyfre" << endl;
        cin >> zmienna;
        if (zmienna.length() != 2)
            throw invalid_argument("podane przez ciebie pole jest albo zajete albo nie istnieje");
        z1 = zmienna[0];
        z2 = zmienna[1];

        if (z2 > z1)
        {
            char pom = z1;
            z1 = z2;
            z2 = pom;

        }
        z1 = toupper(z1);




        if (rozmiar == 4) {
            if ((int) z2 > '4' or (int) z2 <= '0' or (int) z1 - 'A' + 1 > 4 or (int) z1 - 'A' + 1 <= 0)
                throw invalid_argument("podane przez ciebie pole nie istnieje");
            pole = ((int) z2 - '1') * 4 + (int) z1 - 'A';
            if (elementy[pole] != " ")
                throw invalid_argument("podane przez ciebie pole jest zajete");
            elementy[pole] = "O";
            licznik++;
        }

        if (rozmiar == 3) {
            if ((int) z2 > '3' or (int) z2 <= '0' or (int) z1 - 'A' + 1 > 3 or (int) z1 - 'A' + 1 <= 0)
                throw invalid_argument("podane przez ciebie pole nie istnieje");
            pole = ((int) z2 - '1') * 3 + (int) z1 - 'A';
            if (elementy[pole] != " ")
                throw invalid_argument("podane przez ciebie pole jest zajete");
            elementy[pole] = "O";
            licznik++;

        }

    }
void Stangry::wyswietlzwyciezce()
{
        if(zwyciezca == 0) cout<<"Mamy remis prosze panstwa"<<endl;
        if(zwyciezca == 1) cout<<"Gratuluje pieknej wygranej"<<endl;
        if(zwyciezca == 2) cout<<"Niestety przegrywasz, nastepnym razem bedzie lepiej"<<endl;
}
    bool Stangry::czykoniec() {


        if (rozmiar == 4)
        {
            //rzedy
            if (elementy[0] == elementy[1] and elementy[2] == elementy[3] and elementy[1] == elementy[3] and
                elementy[0] != " ")
            {
                if (elementy[0]=="O") zwyciezca = 1;
                else zwyciezca = 2;
                return true;
            }

            if (elementy[4] == elementy[5] and elementy[6] == elementy[7] and elementy[5] == elementy[6] and
                elementy[4] != " ")
            {
                if (elementy[4]=="O") zwyciezca = 1;
                else zwyciezca = 2;
                return true;
            }
            if (elementy[8] == elementy[9] and elementy[10] == elementy[11] and elementy[9] == elementy[10] and
                elementy[8] != " ")
            {
                if (elementy[8]=="O") zwyciezca = 1;
                else zwyciezca = 2;
                return true;
            }
            if (elementy[12] == elementy[13] and elementy[14] == elementy[15] and elementy[13] == elementy[15] and
                elementy[12] != " ")
            {
                if (elementy[12]=="O") zwyciezca = 1;
                else zwyciezca = 2;
                return true;
            }
            //kolumny
            if (elementy[0] == elementy[4] and elementy[8] == elementy[12] and elementy[4] == elementy[8] and
                elementy[0] != " ")
            {
                if (elementy[0]=="O") zwyciezca = 1;
                else zwyciezca = 2;
                return true;
            }
            if (elementy[1] == elementy[5] and elementy[9] == elementy[13] and elementy[5] == elementy[9] and
                elementy[1] != " ")
            {
                if (elementy[1]=="O") zwyciezca = 1;
                else zwyciezca = 2;
                return true;
            }
            if (elementy[2] == elementy[6] and elementy[10] == elementy[14] and elementy[6] == elementy[10] and
                elementy[2] != " ")
            {
                if (elementy[2]=="O") zwyciezca = 1;
                else zwyciezca = 2;
                return true;
            }
            if (elementy[3] == elementy[7] and elementy[11] == elementy[15] and elementy[7] == elementy[11] and
                elementy[3] != " ")
            {
                if (elementy[3]=="O") zwyciezca = 1;
                else zwyciezca = 2;
                return true;
            }
            //skos
            if (elementy[0] == elementy[5] and elementy[10] == elementy[15] and elementy[5] == elementy[10] and
                elementy[0] != " ")
            {
                if (elementy[0]=="O") zwyciezca = 1;
                else zwyciezca = 2;
                return true;
            }
            if (elementy[3] == elementy[6] and elementy[9] == elementy[12] and elementy[6] == elementy[9] and
                elementy[3] != " ")
            {
                if (elementy[3]=="O") zwyciezca = 1;
                else zwyciezca = 2;
                return true;
            }

            if (licznik == rozmiar * rozmiar)
                return true;
            return false;

        }

        if (rozmiar == 3)
        {
            //rzedy
            if (elementy[0] == elementy[1] and elementy[1] == elementy[2]  and elementy[0] != " ")
            {
                if (elementy[0]=="O") zwyciezca = 1;
                else zwyciezca = 2;
                return true;
            }

            if (elementy[3] == elementy[4] and elementy[4] == elementy[5]  and elementy[3] != " ")
            {
                if (elementy[3]=="O") zwyciezca = 1;
                else zwyciezca = 2;
                return true;
            }

            if (elementy[6] == elementy[7] and elementy[7] == elementy[8]  and elementy[6] != " ")
            {
                if (elementy[6]=="O") zwyciezca = 1;
                else zwyciezca = 2;
                return true;
            }
            //kolumny
            if (elementy[0] == elementy[3] and elementy[3] == elementy[6]  and elementy[0] != " ")
            {
                if (elementy[0]=="O") zwyciezca = 1;
                else zwyciezca = 2;
                return true;
            }

            if (elementy[1] == elementy[4] and elementy[4] == elementy[7]  and elementy[1] != " ")
            {
                if (elementy[1]=="O") zwyciezca = 1;
                else zwyciezca = 2;
                return true;
            }

            if (elementy[2] == elementy[5] and elementy[5] == elementy[8]  and elementy[2] != " ")
            {
                if (elementy[2]=="O") zwyciezca = 1;
                else zwyciezca = 2;
                return true;
            }
            //skos
            if (elementy[0] == elementy[4] and elementy[4] == elementy[8]  and elementy[0] != " ")
            {
                if (elementy[0]=="O") zwyciezca = 1;
                else zwyciezca = 2;
                return true;
            }

            if (elementy[2] == elementy[4] and elementy[4] == elementy[6]  and elementy[2] != " ")
            {
                if (elementy[2]=="O") zwyciezca = 1;
                else zwyciezca = 2;
                return true;
            }
            if (licznik == rozmiar * rozmiar)
                return true;
            return false;

        }
    }
}

