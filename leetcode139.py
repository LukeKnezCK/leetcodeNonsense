class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        sequenceCheck = [False] * len(s)
        for letter in range(len(s)):
            for word in wordDict:
                if word == s[letter-len(word)+1 : letter+1] and (sequenceCheck[letter-len(word)] or letter-len(word) == -1):
                    sequenceCheck[letter] = True
        return sequenceCheck[-1]