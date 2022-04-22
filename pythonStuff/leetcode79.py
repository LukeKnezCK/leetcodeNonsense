#My slow solution
class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        list(word)
        for xCord, x in enumerate(board):
            for yCord, y in enumerate(x):
                if y == word[0]:
                    if self.existHelper(Solution, board, word[1:], xCord, yCord, [[xCord,yCord]]):
                        return True
        return False
    
    def existHelper(self, board: list[list[str]], word: list, x: int, y: int, usedLetters: list[list[int]]) -> bool:
        if len(word) == 0:
            return True
        searchDirections = [[x-1,y],[x,y+1],[x+1,y],[x,y-1]]
        for direction in searchDirections:
            if direction[0] < 0 or direction[1] < 0 or direction[1] > len(board[0])-1 or  direction[0] > len(board)-1 or direction in usedLetters:
                continue
            else:
                if board[direction[0]][direction[1]] == word[0]:
                    usedLetters.append([direction[0],direction[1]])
                    if self.existHelper(Solution, board, word[1:], direction[0], direction[1]):
                        return True
                    usedLetters.pop()
        return False

Solution.exist(Solution,[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"SEE")

#Faster solution ://
class Solution:
    def exist(self, board, word):
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    # check whether can find word, start at (i,j) position    
    def dfs(self, board, i, j, word):
        if len(word) == 0: # all the characters are checked
            return True
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
            return False
        tmp = board[i][j]  # first character is found, check the remaining part
        board[i][j] = "#"  # avoid visit agian 
        # check whether can find "word" along one direction
        res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) \
        or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])
        board[i][j] = tmp
        return res
            