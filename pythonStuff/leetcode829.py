class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        counter, result = 1, 0
        while n > counter * (counter-1) // 2:
            if (n - counter * (counter-1) // 2) % counter == 0:
                result += 1
            counter += 1
        return result