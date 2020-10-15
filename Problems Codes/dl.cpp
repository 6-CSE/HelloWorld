#include <bits/stdc++.h> 
using namespace std;

int main(){
	int t;
	cin>>t;
	for(int i=0; i<t; i++){
		int n;
		cin>>n;
		int cost = 0;
		while(n!=2){
			if(n%2==0){
				n = n/2;
				cost = cost + 2;
			}
			else{
				n = n-1;
				cost = cost + 1;
			}
		}
		cost = cost + 2;
		cout<<cost;
	}
}