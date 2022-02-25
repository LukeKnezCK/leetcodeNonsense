class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = {}
        for word in strs:
            #This part is important, sorted returns a list which is unhashable so we
            #must convert it to a tuple to insert it into the dictionary
            letters = tuple(sorted(word))
            groups[letters] = groups.get(letters, []) + [word]
        return list(groups.values())


print(Solution.groupAnagrams(Solution,["eat","tea","tan","ate","nat","bat"]))
