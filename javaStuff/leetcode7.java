class Solution {
    public int reverse(int x) {
        int result = 0;
        while(x != 0){
            int lastPlace = x % 10;
            int holder = result*10 + lastPlace;
            if((holder - lastPlace) / 10 != result){
                return 0;
            }
            result = holder;
            x/=10;
        }
        return result;
    }
}
