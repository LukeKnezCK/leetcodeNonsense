class Solution {
    public List<String> letterCombinations(String digits) {
        LinkedList<String> result = new LinkedList<>();
        if(digits.isEmpty()){
            return result;    
        }
        String[] letters = {"0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        result.add("");
        for (int i = 0; i < digits.length(); i++){
            int x = Character.getNumericValue(digits.charAt(i));
            while(result.peek().length()==i){
                String t = result.remove();
                for(char s : letters[x].toCharArray()){
                    result.add(t+s);
                }
            }
        }
        return result;
    }
}