class Solution {
    public int[] countBits(int n) {
        int[] result = new int[n+1];
        for(int i = 0; i <= n; i++){
            result[i] = bitHelper(i, result);
        }
        return result;
    }
    public int bitHelper(int n, int[] res){
        if(n == 0) return 0;
        if(n == 1) return 1;
        if(res[n] != 0) return res[n];
        if(n%2 == 0){
            return res[n] = bitHelper(n/2,res);
        }
        else{
            return res[n] = 1 + bitHelper(n/2,res);
        }
    }
}