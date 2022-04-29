
import java.util.HashMap;
import java.util.ArrayList;

class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        
        HashMap<Integer, Integer> intersects = new HashMap<Integer, Integer>();
        ArrayList<Integer> results = new ArrayList<Integer>();
        
        for(int x=0; x < nums1.length; x++){
            if(intersects.containsKey(nums1[x])){
                intersects.put(nums1[x], intersects.get(nums1[x])+1);
            }
            else{
                intersects.put(nums1[x], 1);    
            }
        }
        
        for(int y=0; y < nums2.length; y++){
            if( intersects.containsKey(nums2[y]) && intersects.get(nums2[y])>0 ){
                results.add(nums2[y]);
                intersects.put(nums2[y],intersects.get(nums2[y])-1);
            }
        }
        
        int[] a = new int[results.size()];
        for(int i=0; i < a.length; i++){
            a[i]=results.get(i);
        }
        
        return a;
    }
}