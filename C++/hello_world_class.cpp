#include <iostream>
using namespace std;

class Myclass{                            
    public:     
        int mynum;        
};

int main(){
    Myclass myobj;
    myobj.mystring = "Hello World!";

    cout << myobj.mystring << endl;

    return 0;
}
