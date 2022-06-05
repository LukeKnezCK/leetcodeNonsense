class Solution {
    public int longestIncreasingPath(int[][] matrix) {
        int[][] memo = new int[matrix.length][matrix[0].length];
        int highest = 0;
        for(int i = 0; i < matrix.length; i++){
            for(int j = 0; j < matrix[0].length; j++){
                highest = Math.max(pathHelper(i,j,matrix,memo),highest);
            }
        }
        return highest;
    }
    private int pathHelper(int x, int y, int[][] matrix, int[][] memo){
        int maxX = matrix.length;
        int maxY = matrix[0].length;
        int up = 0, down = 0, left = 0, right = 0, holder = 0, maxPath = 0;
        if(x-1 >= 0 && matrix[x][y] < matrix[x-1][y]){
            if(memo[x-1][y] > 0) up = memo[x-1][y];
            else{
                holder = matrix[x][y];
                matrix[x][y] = -1;
                up = pathHelper(x-1, y, matrix, memo);
                matrix[x][y] = holder;
            }
        }
        if(x+1 < maxX && matrix[x][y] < matrix[x+1][y]){
            if( memo[x+1][y] > 0) down =  memo[x+1][y];
            else{
                holder = matrix[x][y];
                matrix[x][y] = -1;
                down = pathHelper(x+1, y, matrix, memo);
                matrix[x][y] = holder;    
            }
        }
        if(y-1 >= 0 && matrix[x][y] < matrix[x][y-1]){
            if(memo[x][y-1] > 0) left = memo[x][y-1];
            else{
                holder = matrix[x][y];
                matrix[x][y] = -1;
                left = pathHelper(x, y-1, matrix, memo);
                matrix[x][y] = holder;    
            }
        }
        if(y+1 < maxY && matrix[x][y] < matrix[x][y+1]){
            if(memo[x][y+1] > 0) right = memo[x][y+1];
            else{
                holder = matrix[x][y];
                matrix[x][y] = -1;
                right = pathHelper(x, y+1, matrix, memo);
                matrix[x][y] = holder;
            }

        }
        maxPath = Math.max(Math.max(up,down),Math.max(left,right));
        if(maxPath == 0){
            memo[x][y] = 1;
            return 1;
        }
        else{
            memo[x][y] = maxPath+1;
            return maxPath+1;    
        }
    }
}