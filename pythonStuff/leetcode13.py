class Solution:
    def romanToInt(self, s: str) -> int:
        key = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        
        s = list(s)
        result = 0
        former = -1
        tracker = 0
        for x in s:
            if key[x] > former and former > 0:
                result += key[x] - tracker
                former = key[x]
                tracker = 0
            elif key[x] < former or former == -1:
                result += tracker
                former = key[x]
                tracker = key[x]
            else:
                tracker += key[x]
        result += tracker
        return result