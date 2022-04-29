import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

class Solution {
    //The super epic fast version
    public int[] fastMaxSlidingWindow(int[] nums, int k){
        if(nums == null || k <= 0){
            return new int[0];
        }
        int numsLength = nums.length;
        int [] results = new int[numsLength-k+1];
        int resultsIndex = 0;
        Deque<Integer> elements = new ArrayDeque<Integer>();
        for (int i = 0; i < numsLength; i++){
            while(!elements.isEmpty() && elements.peek() < i - k + 1){
                elements.poll();
            }
            while(!elements.isEmpty() && nums[elements.peekLast()] < nums[i]){
                elements.pollLast();
            }
            elements.offer(i);
            if(i >= k - 1){
                results[resultsIndex++] = nums[elements.peek()];
            }
        }
        return results;
    }

    //My slow solution :p
    public int[] slowMaxSlidingWindow(int[] nums, int k) {
        List<Integer> results = new ArrayList<Integer>();
        Queue<Integer> currentWindow = new LinkedList<Integer>();
        
        for(int i = 0; i < k; i++){
            currentWindow.add(nums[i]);
        }
        
        int x = k;
        while(x < nums.length){
            Integer currentMax = currentWindow.peek();
            for (Integer element : currentWindow){
                if(element > currentMax){
                    currentMax = element;
                }
            }
            results.add(currentMax);
            currentWindow.remove();
            currentWindow.add(nums[x]);
            x++;
        }
        
        Integer currentMax = currentWindow.peek();
        for (Integer element : currentWindow){
            if(element > currentMax){
                currentMax = element;
            }
        }
        results.add(currentMax);
        
        int[] convert = results.stream().mapToInt(i -> i).toArray();
        return convert;
    }
}