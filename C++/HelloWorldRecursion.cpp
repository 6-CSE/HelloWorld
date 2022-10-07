#include <bits/stdc++.h>
using namespace std;

string hello = "Hello World";

void print_hello(string s,int length,int index){
   
   if(index == length){
      cout <<endl;
      return;
   }
   
   cout<<s[index];
   print_hello(s, length, index+1);
}


int main(){

    print_hello(hello, hello.length(), 0);
    return 0;
}
