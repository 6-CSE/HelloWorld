#include<bits/stdc++.h>

using namespace std;

unsigned int countSetBits(unsigned int n) 
{ 
    unsigned int count = 0; 
    while (n) { 
        count += n & 1; 
        n >>= 1; 
    } 
    return count; 
} 

int main(){
	int t;
	cin>>t;
	for(int i=0; i<t; i++){
		int n,q;
		cin>>n>>q;
		int a[n];
		for(int j=0; j<n; j++){
			cin>>a[j];
		}
		int p[q];
		for(int j=0; j<q; j++){
			cin>>p[j];
		}
		int even[q]={0};
		int odd[q]={0};

		for(int j=0; j<q; j++){
			long long int b[n];
			for(int k=0; k<n; k++){
				b[k] = a[k]^p[j];
			}
			for(int k=0; k<n; k++){
				if(countSetBits(b[k])%2==0){
					even[j]++;
				}
				else{
					odd[j]++;
				}
			}
			cout<<even[j]<<' '<<odd[j]<<endl;
		}
	}
	return 0;
}