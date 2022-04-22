class Solution:
    def numSquares(self, n: int) -> int:
        if n < 2:
            return n
        i = 1
        squares = []
        while i*i <= n:
            squares.append(i*i)
            i+=1
        bfsSet = {n}
        count = 0
        while bfsSet:
            tempSet = set()
            count += 1
            for x in bfsSet:
                for y in squares:
                    if x == y:
                        return count
                    if x < y:
                        break
                    tempSet.add(x-y)
            bfsSet = tempSet
        return cnt
