
#include <iostream>

std::string hello="Hello World";

void print_hello(std::string s,int length,int index)
{
   if(index==length)
      {
         std::cout<<std::endl;
         return;
      }
   std::cout<<s[index];
   print_hello(s,length,index+1);
}


int main() 
{
    print_hello(hello,hello.length(),0);
    return 0;
}
