class Solution {
    public int maxScore(int[] cardPoints, int k) {
        int leftPointer = 0;
        int rightPointer = 0;
        for(int i=cardPoints.length-1;i>=cardPoints.length-k;i--) {
            rightPointer+=cardPoints[i];
        }
        int result = rightPointer;
        int i=-1;
        int j=cardPoints.length-k-1;
        for(int m=1;m<=k;m++) {
            i++;j++;
            leftPointer+=cardPoints[i];
            rightPointer-=cardPoints[j];
            result = Math.max(result, leftPointer+rightPointer);
        }
        return result;
    }
}
