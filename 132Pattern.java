class Solution {
    public boolean find132pattern(int[] nums) {

         int n = nums.length;
        int num3 = Integer.MIN_VALUE;
        Stack<Integer> stack = new Stack<>();

        for (int i = n - 1; i >= 0; i--) {
            if (nums[i] < num3) {
                return true;
            }

            while (!stack.isEmpty() && nums[i] > stack.peek()) {
                num3 = stack.pop();
            }
            stack.push(nums[i]);
        }

        return false;
        
    }
}
