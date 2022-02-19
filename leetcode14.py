def longestCommonPrefix(self, strs: List[str]) -> str:
        firstWord = list(strs[0])
        currentPrefix = ""
        storage = {}
        for y in range(1, len(strs)):
            storage[y] = list(strs[y])
        for x in range(len(firstWord)):
            for y in range(1, len(strs)):
                if x > len(storage[y])-1:
                    return currentPrefix
                elif storage[y][x] != firstWord[x]:
                    return currentPrefix
            currentPrefix += firstWord[x]
        return currentPrefix