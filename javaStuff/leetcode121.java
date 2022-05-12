class Solution {
    public int maxProfit(int[] prices) {
        int leftPointer = 0;
        int rightPointer = 1;
        int maxProfit = 0;
        while(rightPointer < prices.length){
            if(prices[leftPointer] < prices[rightPointer])
                maxProfit = Math.max(prices[rightPointer] - prices[leftPointer], maxProfit);
            else leftPointer = rightPointer;
            rightPointer++;
        }
        return maxProfit;
    }
}