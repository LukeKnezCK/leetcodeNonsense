class Solution {
    public List<List<Integer>> combinationSum3(int k, int n) {
        List<List<Integer>> result = new ArrayList<>();
        combo(result, new ArrayList<Integer>(), k, 1, n);
        return result;
    }
    
    private void combo(List<List<Integer>> result, List<Integer>comb, int k, int start, int n){
        if(comb.size() > k){
            return;
        }
        if(comb.size() == k && n == 0){
            List<Integer> li = new ArrayList<Integer>(comb);
            result.add(li);
            return;
        }
        for(int i = start; i <= n && i <= 9; i++){
            comb.add(i);
            combo(result, comb, k, i+1, n-i);
            comb.remove(comb.size()-1);
        }
    }
}