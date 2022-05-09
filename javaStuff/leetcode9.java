class Solution {
    public boolean isPalindrome(int x) {
        String numberString = Integer.toString(x);
        int leftPointer = 0;
        int rightPointer = numberString.length()-1;
        while(leftPointer < rightPointer){
            if (numberString.charAt(leftPointer) == numberString.charAt(rightPointer)){
                leftPointer++;
                rightPointer--;
            }
            else{
                return false;
            }
        }
        return true;
    }
}