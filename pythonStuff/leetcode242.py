class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        
        for letter in s:
            if letter not in t:
                return False
            else:
                t.remove(letter)
        if len(t) > 0:
            return False
        return True