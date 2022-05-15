class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> letters = new HashMap<>();
        for(int i = 0; i < s.length(); i++){
            char letter = s.charAt(i);
            if(letters.containsKey(letter)){
                letters.replace(letter, letters.get(letter)+1);
            }
            else letters.put(letter, 1);
        }
        for(int i = 0; i < t.length(); i++){
            char letter = t.charAt(i);
            if(letters.containsKey(letter)){
                if(letters.get(letter)>1){
                    letters.replace(letter, letters.get(letter)-1);
                }
                else letters.remove(letter);
            }
            else return false;
        }
        if(letters.size()==0) return true;
        return false;
    }
}
