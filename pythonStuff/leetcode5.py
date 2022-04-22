def longestPalindrome(s: str) -> str:
        if len(s) == 1:
            return s
        convertedString = list(s)
        highScore = []
        for x in range(len(convertedString)):
            current = helper(convertedString, x, x)
            if len(current) > len(highScore):
                highScore = current
            current = helper(convertedString, x, x+1)
            if len(current) > len(highScore):
                highScore = current
        return ''.join(highScore)

def helper(s, l, r) -> str:
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l+1:r]       

longestPalindrome("cbbd")