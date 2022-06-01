class Solution {
    public int longestValidParentheses(String s) {
        int sLength = s.length();
        int highest = 0;
        Stack<Integer> parens = new Stack<>();
        for(int i = 0; i < sLength; i++){
            if(s.charAt(i) == '(') parens.push(i);
            else{
                if(!parens.isEmpty()){
                    if(s.charAt(parens.peek()) == '(') parens.pop();
                    else parens.push(i);
                }
                else parens.push(i);
            }
        }
        if(parens.isEmpty()) highest = sLength;
        else{
            int m = sLength;
            int n = 0;
            while(!parens.isEmpty()){
                n = parens.pop();
                highest = Math.max(highest, m-n-1);
                m = n;
            }
            highest = Math.max(highest,m);
        }
        return highest;
    }
}