#Big shoutout to this legendary man https://www.youtube.com/watch?v=M8BYckxI8_U

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        
        top = (n-1) + (m-1)
        bottom = m - 1
        
        topFactorial = top-1
        bottomFactorial = bottom-1
        for x in range(1,bottom):
            top *= topFactorial
            topFactorial -= 1
        for y in range(1,bottom):
            bottom *= bottomFactorial
            bottomFactorial -= 1
        return top//bottom