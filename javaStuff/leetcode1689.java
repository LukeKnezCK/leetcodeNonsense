class Solution {
    public int minPartitions(String n) {
        int result = 0;
        for(int i = 0; i < n.length(); i++){
            if(Integer.parseInt(String.valueOf(n.charAt(i))) > result) result = Integer.parseInt(String.valueOf(n.charAt(i)));
        }
        return result;
    }
}