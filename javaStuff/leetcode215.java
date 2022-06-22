class Solution {
    public int findKthLargest(int[] nums, int k) {
        List<Integer> numList = new ArrayList<>();
        for(int i : nums) numList.add(i);
        List<Integer> result = mergeSort(numList);
        System.out.println(result);
        return result.get(result.size()-k);
    }
    private List<Integer> mergeSort(List<Integer> numList){
        if(numList.size() <= 1){
            return numList;
        }
        List<Integer> leftList = mergeSort(numList.subList(0, numList.size()/2));
        List<Integer> rightList = mergeSort(numList.subList(numList.size()/2, numList.size()));
        int leftPointer = 0, rightPointer = 0;
        List<Integer> result = new ArrayList<>();
        while(leftPointer < leftList.size() && rightPointer < rightList.size()){
            if(leftList.get(leftPointer) < rightList.get(rightPointer)){
                result.add(leftList.get(leftPointer));
                leftPointer++;
            }
            else{
                result.add(rightList.get(rightPointer));
                rightPointer++;
            }
        }
        while(leftPointer < leftList.size()){
            result.add(leftList.get(leftPointer));
            leftPointer++;
        }
        while(rightPointer < rightList.size()){
            result.add(rightList.get(rightPointer));
            rightPointer++;
        }
        return result;
    }
}