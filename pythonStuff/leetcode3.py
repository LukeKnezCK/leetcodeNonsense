class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        convertedList = list(s)
        highestCombo = 0
        currentCombo = 0
        foundLetters = []
        for x in convertedList:
            if (x in foundLetters):
                if (currentCombo > highestCombo):
                    highestCombo = currentCombo
                for y in convertedList:
                    currentCombo-=1
                    if(foundLetters[0] == x):
                        z = foundLetters.pop(0)
                        foundLetters.append(z)
                        currentCombo += 1
                        break
                    foundLetters.pop(0)
            else:
                currentCombo += 1
                foundLetters.append(x)
        if (currentCombo > highestCombo):
            highestCombo = currentCombo
        return highestCombo