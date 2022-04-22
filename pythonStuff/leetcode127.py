import collections

class Solution():
    def ladderLength2(self, beginWord, endWord, wordList) -> int:
        #Lookup time for set much better than list
        wordList = set(wordList)  
        #Double ended queue, better time complexity for popping from the left
        queue = collections.deque([beginWord,1])
        while queue:
            #get the word we want to work with and the number of transitions we've had so far
            word = queue.popleft()
            length = queue.popleft()
            #Case where we have found a path to our end word
            if word == endWord:
                return length
            #for each letter in our word
            for x in range(len(word)):
                #replace each character with all permutations
                for character in 'abcdefghijklmnopqrstuvwxyz':
                    nextWord = word[:x] + character + word[x+1:]
                    #if that combo matches a word in our list add it to the queue
                    if nextWord in wordList:
                        wordList.remove(nextWord)
                        queue.append(nextWord)
                        queue.append(length+1)
        #if we havent matched our end word then there is no possible path
        return 0

Solution.ladderLength2(Solution, "hit", "cog", ["hot","dot","dog","lot","log","cog"])