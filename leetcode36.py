class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        columnTracker = {
            0: [],
            1: [],
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
            7: [],
            8: []
        }
        subBoxTracker = {
            '00': [],
            '03': [],
            '06': [],
            '30': [],
            '33': [],
            '36': [],
            '60': [],
            '63': [],
            '66': []
        }
        rowTracker = []

        #TODO Switch x and y variables around for easier understanding
        for x in range(9):
            for y in range(9):
                if board[x][y] in rowTracker:
                    return False
                elif board[x][y] in columnTracker[y]:
                    return False
                else:
                    if board[x][y] != ".":
                        rowTracker.append(board[x][y])
                        columnTracker[y].append(board[x][y])
            rowTracker.clear()

        for i in (0,3,6):
            for j in (0,3,6):
                box = str(i) + str(j)
                for l in range(i, i+3):
                    for k in range(j, j+3):
                        if board[l][k] in subBoxTracker[box]:
                            return False
                        else:
                            if board[l][k] != ".":
                                subBoxTracker[box].append(board[l][k])
        return True

Solution.isValidSudoku(Solution,[
    [".",".",".",".","5",".",".","1","."],
    [".","4",".","3",".",".",".",".","."],
    [".",".",".",".",".","3",".",".","1"],
    ["8",".",".",".",".",".",".","2","."],
    [".",".","2",".","7",".",".",".","."],
    [".","1","5",".",".",".",".",".","."],
    [".",".",".",".",".","2",".",".","."],
    [".","2",".","9",".",".",".",".","."],
    [".",".","4",".",".",".",".",".","."]])