#include<iostream>
using namespace std;

string greet_hello()
{
  return "hello";
}

string greet_world()
{
  return "world";
}

int main()
{
   string str = greet_hello() + greet_world();
    cout<<str;
   return 0;
}
