class Solution:
    def mySqrt(self, x: int) -> int:
        y = 2
        result = 1
        if x < 2:
            return x
        while y <= 46340:
            if y*y <= x:
                if y > result:
                    result = y
                y += 1
            else:
                return result
        return result