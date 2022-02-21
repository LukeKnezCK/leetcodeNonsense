class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if (dividend < 0) == (divisor < 0):
            signed = False
        else:
            signed = True
        dividend, divisor = abs(dividend), abs(divisor)
        counter = 0
        while divisor <= dividend:
            increaser, i = divisor, 1
            while increaser <= dividend:
                dividend -= increaser
                counter += i
                i <<= 1
                increaser <<= 1
        if signed:
            counter = counter*-1
        return min(max(-2147483648, counter), 2147483647)