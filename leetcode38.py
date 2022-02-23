class Solution:
    def countAndSay(self, n:int) -> str:
        baseCase = "1"
        if n == 1:
            return baseCase
        else:
            return self.countAndSayHelper(baseCase,n-1)

    def countAndSayHelper(self, lastString: str, n:int) -> str:
        if n == 0:
            return lastString
        convertedList= list(lastString)
        current = convertedList[0]
        occurences = 0
        constructedString = ""
        for x in convertedList:
            if x == current:
                occurences += 1
            else:
                constructedString += (str(occurences) + str(current))
                current = x
                occurences = 1
        constructedString += (str(occurences) + str(current))
        return self.countAndSayHelper(constructedString, n-1)