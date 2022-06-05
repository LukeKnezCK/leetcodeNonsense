class Solution {
    public int totalNQueens(int n) {
        char[][] combo = new char[n][n];
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                combo[i][j] = '.';
            }
        }
        boolean [] col = new boolean[n], diagL = new boolean[2*n-1], diagR = new boolean[2*n-1];
        return queensHelper(combo, 0, n, col, diagL, diagR);
    }
    
    private int queensHelper(char[][] combo, int layer, int n, boolean[] col, boolean[] diagL, boolean[] diagR){
        if(layer == n){
            return 1;
        }
        int counter = 0;
        for(int j = 0; j < n; j++){
            if(col[j] || diagL[layer+n-j-1]|| diagR[layer+j]) continue;
            col[j] = true;
            diagL[layer + n - j - 1] = true;
            diagR[layer + j] = true;
            combo[layer][j] = 'Q';
            counter += queensHelper(combo, layer + 1, n, col, diagL, diagR);
            combo[layer][j] = '.';
            col[j] = false;
            diagL[layer + n - j - 1] = false;
            diagR[layer + j] = false;
        }
        return counter;
    }
}