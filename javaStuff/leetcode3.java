class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s.length() == 0) return 0;
        HashMap<Character, Integer> counter = new HashMap<>();
        int max = 0;
        for(int i = 0, j = 0; i<s.length(); ++i){
            if(counter.containsKey(s.charAt(i))){
                j = Math.max(j,counter.get(s.charAt(i))+1);
            }
            counter.put(s.charAt(i),i);
            max = Math.max(max, i-j+1);
        }
        return max;
    }
}
