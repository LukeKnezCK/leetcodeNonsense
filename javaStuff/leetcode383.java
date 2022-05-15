class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        HashMap<Character, Integer> ransomLetters = new HashMap<>();
        for (int i = 0; i < ransomNote.length(); i++){
            char letter = ransomNote.charAt(i);
            if(ransomLetters.containsKey(letter)){
                ransomLetters.replace(letter,ransomLetters.get(letter)+1);
            }
            else ransomLetters.put(letter,1);
        }
        for(int j = 0; j < magazine.length(); j++){
            char letter = magazine.charAt(j);
            if(ransomLetters.containsKey(letter)){
                if(ransomLetters.get(letter)>1){
                    ransomLetters.replace(letter,ransomLetters.get(letter)-1);
                }
                else ransomLetters.remove(letter);
            }
        }
        if(ransomLetters.size() > 0){
            return false;
        }
        return true;
    }
}
