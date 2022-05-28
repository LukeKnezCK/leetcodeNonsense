class Solution {
    public int missingNumber(int[] nums) {
        int counter = 1;
        int holder = 0;
        int subtractor = 0;
        for(int i = 0; i < nums.length; i++){
            holder += counter;
            counter++;
            subtractor += nums[i];
        }
        return holder - subtractor;
    }
}