class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for y, row in enumerate(grid):
            for x, column in enumerate(grid[y]):
                if grid[y][x] == "1":
                    count += 1
                    self.markIslands(x,y,grid)
        return count
    
    def markIslands(self,x,y,grid):
        if x >= len(grid[0]) or x < 0:
            return
        if y >= len(grid) or y < 0:
            return
        if grid[y][x] == "1":
            grid[y][x] = "M"
            self.markIslands(x+1,y,grid)
            self.markIslands(x-1,y,grid)
            self.markIslands(x,y+1,grid)
            self.markIslands(x,y-1,grid)
        return