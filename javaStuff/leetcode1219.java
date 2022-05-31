class Solution {
    public int getMaximumGold(int[][] grid) {
        int maximum = 0;
        for(int y = 0; y < grid.length; y++){
            for(int x = 0; x < grid[0].length; x++){
                maximum = Math.max(maximum, maxRecursHelper(x,y,grid,0));
            }
        }
        return maximum;
    }
    private int maxRecursHelper(int x, int y, int[][] grid, int count){
        if(y < 0 || y>= grid.length)return 0;
        if(x < 0 || x>= grid[0].length)return 0;
        if(grid[y][x] == 0) return count;
        int holder = grid[y][x];
        grid[y][x] = 0;
        int up = maxRecursHelper(x,y-1,grid,count);
        int right = maxRecursHelper(x+1,y,grid,count);
        int down = maxRecursHelper(x,y+1,grid,count);
        int left = maxRecursHelper(x-1,y,grid,count);
        int bestPath = Math.max(Math.max(up, right), Math.max(down, left));
        grid[y][x] = holder;
        return grid[y][x] + count + bestPath;
    }
}