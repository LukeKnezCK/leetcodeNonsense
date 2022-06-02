class Solution {
    public boolean validMountainArray(int[] arr) {
        if(arr.length < 3) return false;
        boolean lever = true;
        boolean increase = false;
        boolean decrease = false;
        for(int i = 1; i < arr.length; i++){
            if(lever){
                if(arr[i] > arr[i-1]){ increase = true; continue;}
                else if(arr[i] == arr[i-1]) return false;
                else {i--; lever = false;}
            }
            else{
                if(arr[i] < arr[i-1]) { decrease = true; continue;}
                else return false;
            }
        }
        return increase && decrease;
    }
}