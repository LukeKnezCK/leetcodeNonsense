class Solution:
    def hammingWeight(self, n: int) -> int:
        n = format(n, 'b')
        count = 0
        for x in n:
            if x == '1':
                count += 1
        return count