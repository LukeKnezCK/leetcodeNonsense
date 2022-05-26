public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        int result = 0;
        String convert = Integer.toBinaryString(n);
        for(int i = 0; i < convert.length(); i++){
            if(convert.charAt(i) == '1') result++;
        }
        return result;
    }
}