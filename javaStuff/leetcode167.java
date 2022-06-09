class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int leftPointer = 0;
        int rightPointer = numbers.length-1;
        int sum = -3001;
        int[] result = new int[2]; 
        while(leftPointer < rightPointer){
            sum = numbers[leftPointer] + numbers[rightPointer];
            if(sum == target){
                result[0] = leftPointer+1;
                result[1] = rightPointer+1;
                return result;
            }
            else if(sum < target) leftPointer++;
            else rightPointer--;
        }
        return null;
    }
}