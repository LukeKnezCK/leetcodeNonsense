class Solution:
    def myAtoi(self, s: str) -> int:
        sList = list(s)
        y = 0
        while y < len(sList) and sList[y] == ' ':
            y+=1
        sList=sList[y:]
        if len(sList) <= 0:
            return 0
        sign = False
        if sList[0] == '-':
            sign = True
            sList.pop(0)
        elif sList[0] == '+':
            sList.pop(0)
        if len(sList) == 0:
            return 0
        y = 0
        while y < len(sList) and sList[y].isnumeric():
            y += 1
        sList = sList[:y]
        if len(sList) == 0:
            return 0
        if not sList[0].isnumeric():
            return 0
        result = int(sList[0])
        sList.pop(0)
        for x in sList:
            if x.isnumeric():
                result *= 10
                result += int(x)
            else:
                break
        if sign:
            result*=-1
        if result <-2147483648:
            return -2147483648
        if result > 2147483647:
            return 2147483647
        return result