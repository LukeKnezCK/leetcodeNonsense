class Solution:
    def isValid(self, s: str) -> bool:
        convertList = list(s)
        bracketTracker = []
        pairings = {
            '}':'{',
            ')':'(',
            ']':'[',
        }
        for x in range(len(s)):
            currentPop = convertList.pop()
            if currentPop in ['}', ']', ')']:
                bracketTracker.append(currentPop)
            elif currentPop in ['{', '[', '(']:
                try:
                    if currentPop != pairings[bracketTracker.pop()]:
                        return False
                except:
                    return False
            else:
                continue
        if len(bracketTracker) == 0:
            return True
        else:
            return False