#include <bits/stdc++.h> 
using namespace std; 
class Solution {
public:
	double num;
    double nthPersonGetsNthSeat(int n) {
        num = 1/n;
        return num;
    }
};
int main(){
    int n;
    cin>>n;
    Solution x;
    double res = x.nthPersonGetsNthSeat(n);
    cout<<res;
    return 0;
}