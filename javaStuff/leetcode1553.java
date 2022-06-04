class Solution {

    //Faster version that uses memoization
    Map<Integer, Integer> memoizer = new HashMap<>();
    public int minDays(int n) {
        if(n <= 1) return n;        
        if(!memoizer.containsKey(n)){
            memoizer.put(n, 1 + Math.min(n % 2 + minDays(n / 2), n % 3 + minDays(n / 3)));
        }
        return memoizer.get(n);
    }

    //My slow version :p
    public int slowMinDays(int n) {
        if(n == 0) return 0;        
        int option1 = minDays(n-1);
        int option2 = Integer.MAX_VALUE;
        if(n % 2 == 0) option2 = minDays(n-(n/2));
        int option3 = Integer.MAX_VALUE;
        if(n % 3 == 0) option3 = minDays(n-(2*(n/3)));
        return Math.min(Math.min(option1,option2),option3)+1;
    }
}