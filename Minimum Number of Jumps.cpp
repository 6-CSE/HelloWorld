/*
Minimum number of jumps Problem
Given an array of N integers arr[] where each element represents the maximum length of the jump that can be made forward from that element. This means if arr[i] = x, then we can jump any distance y such that y ≤ x.
Find the minimum number of jumps to reach the end of the array (starting from the first element). If an element is 0, then you cannot move through that element. Return -1 if you can't reach the end of the array.
Input:
N = 11 
arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9} 
Output: 3 
Explanation: 
First jump from 1st element to 2nd 
element with value 3. Now, from here 
we jump to 5th element with value 9, 
and from here we will jump to the last. 
*/

#include<bits/stdc++.h>
using namespace std;
// Function to return minimum number of jumps to end of array

class Solution{
  public:
    int minJumps(int arr[], int n){
       int steps = 0;
       int curr_pos = 0;
       int max_step = arr[0];
       int curr_to_max=curr_pos+1;
       int max_possible_value = 0;
       int max_possible_value_index = 0;

       while(1){
           if(max_step>=n-1){
               return steps+1;
           }
           if(curr_to_max<=max_step){
               if(max_possible_value<curr_to_max+arr[curr_to_max]){
                   max_possible_value = curr_to_max+arr[curr_to_max];
                   max_possible_value_index = curr_to_max;
               }
               curr_to_max++;
           }else{
               if(max_possible_value<=max_step) return -1;
               curr_pos = max_possible_value_index;
               max_step = max_possible_value;
               curr_to_max=curr_pos+1;
               steps++;
           }
       }
       return -1;
    }
};
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n,i,j;
        cin>>n;
        int arr[n];
        for(int i=0; i<n; i++)
            cin>>arr[i];
        Solution obj;
        cout<<obj.minJumps(arr, n)<<endl;
    }
    return 0;
}
