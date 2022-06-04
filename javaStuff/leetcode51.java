class Solution {
    public List<List<String>> solveNQueens(int n) {
        List<List<String>> results = new ArrayList<List<String>>();
        char[][] combo = new char[n][n];
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                combo[i][j] = '.';
            }
        }
        boolean [] col = new boolean[n], diagL = new boolean[2*n-1], diagR = new boolean[2*n-1];
        queensHelper(combo, 0, n, results, col, diagL, diagR);
        return results;
    }
    
    private void queensHelper(char[][] combo, int layer, int n, List<List<String>> results, boolean[] col, boolean[] diagL, boolean[] diagR){
        if(layer == n){
            List<String> valid = new ArrayList<>();
            for(int i = 0; i < n; i++){
                valid.add(String.valueOf(combo[i]));
            }
            results.add(valid);
            return;
        }
        for(int j = 0; j < n; j++){
            if(col[j] || diagL[layer+n-j-1]|| diagR[layer+j]) continue;
            col[j] = true;
            diagL[layer + n - j - 1] = true;
            diagR[layer + j] = true;
            combo[layer][j] = 'Q';
            queensHelper(combo, layer + 1, n, results, col, diagL, diagR);
            combo[layer][j] = '.';
            col[j] = false;
            diagL[layer + n - j - 1] = false;
            diagR[layer + j] = false;
        }
    }
}