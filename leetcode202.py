class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        encounteredNums = set()
        
        def happyHelper(n):
            nonlocal encounteredNums
            if n == 1:
                return True
            n = str(n)
            sum = 0
            for x in n:
                x = int(x)
                sum += x*x
            if sum in encounteredNums:
                return False
            encounteredNums.add(sum)
            return happyHelper(sum)
        
        n = str(n)
        sum = 0
        for x in n:
            x = int(x)
            sum += x*x
        encounteredNums.add(sum)
        return happyHelper(sum)
    