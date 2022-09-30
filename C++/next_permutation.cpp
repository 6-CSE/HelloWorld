class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        if(nums.size() == 0 || nums.size() == 1) return;
        int i,index1=-1,index2=-1,temp;
        for(i=nums.size()-1;i>0;i--){
            cout << nums[i] << " " << nums[i-1] << endl;
            if(nums[i] > nums[i-1]){ 
                index1 = i-1;
                break;
            }
        }
        if(index1!=-1){
        for(i=nums.size()-1;i>=0;i--){
            if(nums[i] > nums[index1]) {
                index2 = i;
                break;
            }
        }
        temp = nums[index1];
        nums[index1] = nums[index2];
        nums[index2] = temp;
        }
        // cout << index1;
        reverse(nums.begin() + index1 + 1, nums.end());
    }
};