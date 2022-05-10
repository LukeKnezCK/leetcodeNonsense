class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> encounters = new HashSet<>();
        for(int x = 0; x < nums.length; x++){
            if(!encounters.add(nums[x])){
                return true;
            }
        }
        return false;
    }
}