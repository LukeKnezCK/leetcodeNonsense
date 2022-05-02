class Solution {
    public int kthSmallest(int[][] matrix, int k) {
        int[] fullList = new int[(matrix.length*matrix[0].length)];
        int counter = 0;
        for(int x = 0; x < matrix.length; x++){
            for(int y = 0; y < matrix[x].length; y++){
                fullList[counter] = matrix[x][y];
                counter++;
            }
        }
        mergeSort(fullList);
        return fullList[k-1];
    }
    
    private static void mergeSort(int[] inputArray){
        int arrayLength = inputArray.length;
        if (arrayLength < 2){
            return;
        }
        int arrayMid = arrayLength / 2;
        int[] leftArray = new int[arrayMid];
        int[] rightArray = new int[arrayLength-arrayMid];
        for (int i = 0; i < arrayMid; i++){
            leftArray[i] = inputArray[i];
        }
        for (int i = arrayMid; i < arrayLength; i++){
            rightArray[i-arrayMid] = inputArray[i];
        }
        mergeSort(leftArray);
        mergeSort(rightArray);
        merge(inputArray, leftArray, rightArray);
    }
    
    private static void merge(int[] inputArray, int[] leftArray, int[] rightArray){
        int leftSize = leftArray.length;
        int rightSize = rightArray.length;
        
        int leftPointer = 0, rightPointer = 0, counter =0;
        while (leftPointer < leftSize && rightPointer < rightSize){
            if (leftArray[leftPointer] <= rightArray[rightPointer]){
                inputArray[counter] = leftArray[leftPointer];
                leftPointer++;
            }
            else{
                inputArray[counter] = rightArray[rightPointer];
                rightPointer++;
            }
            counter++;
        }
        while (leftPointer < leftSize){
            inputArray[counter] = leftArray[leftPointer];
            leftPointer++;
            counter++;
        }
        while (rightPointer < rightSize){
            inputArray[counter] = rightArray[rightPointer];
            rightPointer++;
            counter++;
        }
    }
}