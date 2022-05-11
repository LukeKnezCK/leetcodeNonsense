class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int[] result = new int[m+n];
        int pointer1 = 0;
        int pointer2 = 0;
        int counter = 0;
        while(pointer1 < m && pointer2 < n){
            if(nums1[pointer1] < nums2[pointer2]){
                result[counter] = nums1[pointer1];
                counter++;
                pointer1++;
            }
            else{
                result[counter] = nums2[pointer2];
                counter++;
                pointer2++;
            }
        }
        while(pointer1 < m){
            result[counter] = nums1[pointer1];
            counter++;
            pointer1++;
        }
        while(pointer2 < n){
            result[counter] = nums2[pointer2];
            counter++;
            pointer2++;
        }
        for(int i = 0; i < nums1.length; i++){
            nums1[i] = result[i];
        }
    }
}
