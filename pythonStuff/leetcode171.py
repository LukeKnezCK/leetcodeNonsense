class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for pos, char in enumerate(columnTitle[::-1]):
            val = ord(char)-64
            ans +=  val*26**pos  
        return ans