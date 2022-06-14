class Solution {
    public int minDistance(String word1, String word2) {
        int[][] checker = new int[word1.length()+1][word2.length()+1];
        for(int i = 1; i <= word1.length(); i++){
            for(int j = 1; j <= word2.length(); j++){
                checker[i][j] = word1.charAt(i-1) == word2.charAt(j-1) ? checker[i-1][j-1] + 1 : Math.max(checker[i-1][j], checker[i][j-1]);
            }
        }
        return word1.length() + word2.length() - 2 * checker[word1.length()][word2.length()];
    }
}