class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        leftPointer = 0
        rightPointer = 1
        maxProfit = 0
        while rightPointer < len(prices):
            if prices[leftPointer] < prices[rightPointer]:
                maxProfit = max(prices[rightPointer] - prices[leftPointer], maxProfit)
            else:
                leftPointer = rightPointer
            rightPointer += 1
        return maxProfit