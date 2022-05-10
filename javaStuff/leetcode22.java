class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> results = new ArrayList<>();
        pHelper(results, "", 0, 0, n);
        return results;
    }
    private void pHelper(List<String> results, String str, int open, int close, int max){
        if(str.length() == max*2){
            results.add(str);
            return;
        }
        if(open < max){
            pHelper(results, str+"(", open+1, close, max);
        }
        if(close < open){
            pHelper(results, str+")", open, close+1, max);
        }
    }
}