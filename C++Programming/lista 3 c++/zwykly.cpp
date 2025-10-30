#include <iostream>
#include <sstream>
using namespace std;

int main() {
    int n,x,y,bloczki0 = 0,bloczki1 = 0;
    string s;
    cin>>n>>x>>y;
    cin>>s;
    int i = 0;
    while (i < s.length()){
        if(s[i] == '1'){
            while(s[i] == '1' && i < s.length()){
                i++;
            }
            bloczki1++;
        }
        if(s[i] == '0'){
            while(s[i] == '0' && i < s.length()){
                i++;
            }
            bloczki0++;
        }
    }
    if(s[0] == '1') bloczki1--;
    if(s[s.length() - 1] == '1') bloczki1--;
    if(bloczki1 < 0) bloczki1 = 0;

    cout<<min(bloczki0 * y, bloczki1 * x + y);

}

