class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        else:
            lowValue = 2
            highValue = 3
            x = 3
            while x < n:
                highValue, lowValue = highValue+lowValue, highValue
                x += 1
            return highValue