class Solution {
    public int maxSubArray(int[] nums) {
        int currentMax = nums[0], maxEnd = nums[0];
        for(int i = 1; i < nums.length; i++){
            maxEnd = Math.max(maxEnd + nums[i], nums[i]);
            currentMax = Math.max(currentMax, maxEnd);
        }
        return currentMax;
    }
}