class Solution {
	public int[] twoSum(int[] nums, int target){
		Map<Integer, Integer> compliments = new HashMap<Integer, Integer>();
		int[] results = {0,0};
		for(int x = 0; x < nums.length; x++){
			int compliment = target - nums[x];
			if (compliments.containsKey(compliment)){
				results[0] = x;
				results[1] = compliments.get(compliment);
				return results;
			}
			else{
				compliments.put(nums[x],x);
			}
		}
		return results;		
	}
}
