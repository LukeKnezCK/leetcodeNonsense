class Solution {
    public boolean backspaceCompare(String s, String t) {
        Stack <Character> word1 = new Stack<>();
        Stack <Character> word2 = new Stack<>();
        for(int i = 0; i < s.length(); i++){
            if(s.charAt(i) == '#'){
                if(!word1.empty()){
                    word1.pop();
                }
            }
            else{
                word1.push(s.charAt(i));
            }
        }
        for(int i = 0; i < t.length(); i++){
            if(t.charAt(i) == '#'){
                if(!word2.empty()){
                    word2.pop();
                }
            }
            else{
                word2.push(t.charAt(i));
            }
        }
        while(!word2.empty() && !word1.empty()){
            if(!(word1.pop() == word2.pop())){
                return false;
            }
        }
        if(word2.empty() && word1.empty()) return true;
        return false;
    }
}