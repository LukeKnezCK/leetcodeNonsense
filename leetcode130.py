class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """   
        
        m = len(board)
        n = len(board[0])
        
        def freeCheck(x,y):
            nonlocal board
            nonlocal m
            nonlocal n
            if x > m-1 or y >n-1 or x < 0 or y < 0:
                return
            elif board[x][y] == "O":
                board[x][y] = "S"
                freeCheck(x+1,y)
                freeCheck(x-1,y)
                freeCheck(x,y+1)
                freeCheck(x,y-1)
            else:
                return
        
        for top in range(n):
            if board[0][top] == "O":
                freeCheck(0,top)
        for right in range(m):
            if board[right][n-1] == "O":
                freeCheck(right,n-1)
        for left in range(m):
            if board[left][0] == "O":
                freeCheck(left,0)
        for bottom in range(n):
            if board[m-1][bottom] == "O":
                freeCheck(m-1,bottom)
                
        for x in range(m):
            for y in range(n):
                if board[x][y] == "O":
                    board[x][y] = "X"
                elif board[x][y] == "S":
                    board[x][y] = "O"
        
        
        
#Initial approach that ended up being wrong because the problem statement
# was garbo and unclear >:p 
        
#         for x in range(m):
#             for y in range(n):
#                 if board[x][y] == "O":
#                     horizontal = False
#                     vertical = False
                    
#                     for i in range(0, y):
#                         if board[x][i] == "X":
#                             for j in range(y, n):
#                                 if board[x][j] == "X":
#                                     horizontal = True
#                                     break
#                             break
                    
#                     for k in range(0, x):
#                         if board[k][y] == "X":
#                             for l in range(x, m):
#                                 if board[l][y] == "X":
#                                     vertical = True
#                                     break
#                             break
                    
#                     if horizontal and vertical:
#                         board[x][y] = "X"