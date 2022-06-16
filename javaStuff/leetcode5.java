class Solution {
    public String longestPalindrome(String s) {
        String high = "";
        for(int i = 0; i <s.length(); i++){
            String count = helper(s,i,i);
            if(high.length() < count.length()) high = count;
            count = helper(s,i,i+1);
            if(high.length() < count.length()) high = count;
        }
        return high;
    }
    public String helper(String s, int l, int r){
        System.out.println(l+" "+r);
        while(l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)){
            l--;
            r++;
        }
        return s.substring(l+1,r);
    }
}