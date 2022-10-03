#include <iostream>
using namespace std;

void rec(int i){
	cout << "Hello" << i << endl;
	for(int j=0;j<5;j++)
	cout << "\tloop" << j << endl;
	rec(i+1);
	if(i<10)
	cout << "setelah rekursif" << endl;
}

int main(){
	cout << "start" << endl;
	rec(0);
	cout << "finish" << endl;
	return 0;
}
