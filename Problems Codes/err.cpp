#include <bits/stdc++.h> 

using namespace std;

int main(){
	int t;
	cin>>t;
	vector<int> arr;
	vector<int> brr;
	vector<int> crr;
	for(int i=0; i<t; i++){
		int n;
		cin>>n;
		arr.push_back(n);
	}
	for(int i=0; i<t-1; i++){
		int n;
		cin>>n;
		brr.push_back(n);
	}
	for(int i=0; i<t-2; i++){
		int n;
		cin>>n;
		crr.push_back(n);
	}
	vector<int>drr = brr;
	for(int i=0; i<t-1; i++){
		arr.erase(remove(arr.begin(), arr.end(), drr[i]), arr.end());
	}
	cout<<arr[0]<<endl;
	for(int i=0; i<t-1; i++){
		brr.erase(remove(brr.begin(), brr.end(), crr[i]), brr.end());
	}
	cout<<brr[0]<<endl;
}