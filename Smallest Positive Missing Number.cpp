/*
Smallest Positive missing number
You are given an array arr[] of N integers. The task is to find the smallest positive number missing from the array.
Note: Positive number starts from 1.
Example:
Input:
N = 5
arr[] = {1,2,3,4,5}
Output: 6
Explanation: Smallest positive missing 
number is 6.
*/

#include<bits/stdc++.h>
using namespace std;
class Solution
{
    public:
    // Function to find the smallest positive number missing from the array.
    int missingNumber(int arr[], int n) 
    { 
        int lowest=INT_MAX;
        for(int i=0;i<n;i++){
            if(arr[i]<lowest and arr[i]>0){
                lowest=arr[i];
            }
        }
        if(lowest>1){
            return 1;
        }
        int maxN=arr[0];
        for(int i=1;i<n;i++){
            if(arr[i]>maxN){maxN=arr[i];}
        }
        int *countArray=new int[maxN+1];
        for(int i=0;i<n;i++){
            if(arr[i]>0){
                countArray[arr[i]]++;
            }
        }
        for(int i=1;i<maxN+1;i++){
            if(countArray[i]==0){
                return i;
            }
        }
        return maxN+1;
        }
};
int missingNumber(int arr[], int n);

int main() { 

    // Taking testcases
    int t;
    cin>>t;
    while(t--){

        // Input number n
        int n;
        cin>>n;
        int arr[n];

        // Adding elements to the array
        for(int i=0; i<n; i++)cin>>arr[i];

        Solution ob;
        // Calling missingNumber()
        cout<<ob.missingNumber(arr, n)<<endl;
    }
    return 0; 
}
