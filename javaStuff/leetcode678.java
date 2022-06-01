class Solution {
    public boolean checkValidString(String s) {
        Stack<Integer> parens = new Stack<>();
        Stack<Integer> wildcards = new Stack<>();
        for(int i = 0; i < s.length(); i++){
            if(s.charAt(i) == '('){
                parens.push(i);
            }
            else if(s.charAt(i) == ')'){
                if(!parens.isEmpty()) parens.pop();
                else if(!wildcards.isEmpty()) wildcards.pop();
                else return false;
            }
            else wildcards.push(i);
        }
        while(!parens.isEmpty() && !wildcards.isEmpty()){
            if(parens.pop() > wildcards.pop()) return false;
        }
        if(!parens.isEmpty()) return false;
        else return true;
    }
}
