#include<iostream>
using namespace std;
class Fahrenheit
{
    float f;
    public:
    Fahrenheit()
    {
        f = 0;
    }
    Fahrenheit(float value)
    {
        f = value;
    }
    friend ostream& operator <<(ostream &, Fahrenheit &);
    friend istream& operator >>(istream &, Fahrenheit &);
    float getData()
    {
        return f;
    }
};
ostream& operator <<(ostream &a, Fahrenheit &b)
{
    a<<b.f;
    return a;
}
istream& operator >>(istream &a, Fahrenheit &b)
{
    a>>b.f;
    return a;
}
class Celsius
{
    float c;
    public:
    Celsius()
    {
        c=0;
    }
    Celsius(float value)
    {
        c = value;
    }
    friend ostream& operator <<(ostream &, Celsius &);
    friend istream& operator >>(istream &, Celsius &);
    Celsius from_fahrenheit(Fahrenheit f)
    {
        float c = ((f.getData()-32)*5)/9;
        return Celsius(c);
    }
};
ostream& operator <<(ostream &a, Celsius &b)
{
    a<<b.c;
    return a;
}
istream& operator >>(istream &a, Celsius &b)
{
    a>>b.c;
    return a;
}

int main()
{
    Celsius C;
    Fahrenheit F;
    cout<<"Enter the value of Celsius:"<<endl;
    cin>>C;
    cout<<"Enter the value of Fahrenheit:"<<endl;
    cin>>F;
    cout<<"The Celsius is:"<<C<<endl;
    cout<<"The Fahrenheit is:"<<F<<endl;
    C = C.from_fahrenheit(F);
    cout<<"The Celsius from Fahrenheit is:"<<C<<endl;
    return 0;
}

