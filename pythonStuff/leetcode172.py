import re
class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 1
        regex = re.compile("0+$")
        while n > 1:
            ans = ans * n
            n -= 1
        result = re.search(regex, str(ans))
        if result == None:
            return 0
        return len(result.group())

#Much better way of doing this. Instead of calculating the factorial just see how many 5's fit in the number
#Dont ask why the 5 thing works because I dont know
    def trailingZeroesOptimized(self, n: int) -> int:
        ans = 0
        while not n == 0:
            ans += n // 5
            n = n // 5
        return ans

#I made it even faster using tail recursion :^)
    def trailingZeroesSUPAFAST(self, n: int) -> int:
        if n == 0:
            return 0
        else:
            return Solution.trailHelper(n//5, n//5)
        
    def trailHelper(self, counter: int, n: int) -> int:
        if n == 0:
            return counter
        else:
            return Solution.trailHelper(counter+n//5, n//5)
