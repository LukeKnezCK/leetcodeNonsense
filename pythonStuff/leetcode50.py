class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            x = 1 / x
            n = abs(n)
            
        result = 1
        while n:
            if n % 2:
                result *= x
            x *= x
            n //= 2
        return result

Solution.myPow(Solution, 2, 10)