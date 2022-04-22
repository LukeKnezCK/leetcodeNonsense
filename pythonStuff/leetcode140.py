class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        res = []
        #improve lookup time by converting list to set O(n) -> O(1)
        wordDict = set(wordDict)

        #Recursive helper function, takes an index of where we are in evaluating the string and the path that we currently have
        def breakHelper(index, path):
            #nonlocals that we want to persist throughout all recursive calls
            nonlocal res, s, wordDict
            #base case for the end of recursion, append our found words then we append our path to the results
            if len(s) == index:
                res.append(' '.join(path))
            #iterate through the word letter by letter
            for i in range(index,len(s)):
                tmp = s[index:i+1]
                #if we find a word then we branch off into another recursive call to pursue that path
                if tmp in wordDict:
                    breakHelper(i+1,path+[tmp])


        breakHelper(0,[])
        return res

Solution.wordBreak(Solution, "catsanddog" , ["cat","cats","and","sand","dog"])