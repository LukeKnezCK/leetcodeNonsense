//faster cool guy solution <@:]
public boolean hasAllCodes(String s, int k) {
        Set<String> seen = new HashSet<>();
        for (int i = k; i <= s.length() && seen.size() < 1 << k; ++i) {
            seen.add(s.substring(i - k, i));
        }
        return seen.size() == 1 << k;
}

//my slowpoke solution >:[
class Solution {
    public boolean hasAllCodes(String s, int k) {
        String a = "1";
        String b = "0";
        return helper(s,k-1,a) && helper(s,k-1,b);
    }
    private boolean helper(String s, int k, String b){
        if(k == 0) return s.contains(b);
        String alt1 = b + "1";
        String alt2 = b + "0";
        return helper(s,k-1,alt1) && helper(s,k-1,alt2);
    }
}
