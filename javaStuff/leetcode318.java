class Solution {
    public int maxProduct(String[] words) {
        HashMap<String,Set<Character>> letters = new HashMap<>();
        for(String x : words){
            letters.put(x, new HashSet<Character>());
            for(int i = 0; i < x.length(); i++){
                letters.get(x).add(x.charAt(i));
            }
        }
        int highest = 0;
        for(int j = 0; j < words.length-1; j++){
            for(int k = j+1; k < words.length; k++){
                Set<Character> intersection = new HashSet<Character>(letters.get(words[j]));
                intersection.retainAll(letters.get(words[k]));
                if(intersection.isEmpty()){
                    highest = Math.max(words[j].length()*words[k].length(), highest);
                }
            }
        }
        return highest;
    }
}