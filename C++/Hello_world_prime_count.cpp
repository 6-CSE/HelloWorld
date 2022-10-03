/*
Given an integer n, return the number of prime numbers that are strictly less than n.
*/

#include <bits/stdc++.h>
using namespace std;

int countPrimes(int n)
{
    int count = 0;
    vector<bool> prime(n + 1, true);
    prime[0] = false;
    prime[1] = false;
    for (int i = 2; i < n; i++)
    {
        if (prime[i])
        {
            count++;
            for (int j = 2 * i; j < n; j += i)
            {
                prime[j] = false;
            }
        }
    }
    return count;
}

int main()
{
    int n;
    cout << "Enter the number : ";
    cin >> n;
    cout << "The number of prime nos less than " << n << " is " << countPrimes(n) << endl;
    for(int i = 0; i < n; i++)
    {
        cout<<"Hello World!"<<endl;
    }
    return 0;
}
