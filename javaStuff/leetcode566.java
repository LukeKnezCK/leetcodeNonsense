class Solution {
    public int[][] matrixReshape(int[][] mat, int r, int c) {
        if(mat.length*mat[0].length != r*c) return mat;
        int[][] result = new int[r][c];
        List<Integer> holder = new ArrayList<>();
        for(int i = 0; i < mat.length; i++){
            for(int j = 0; j < mat[0].length; j++){
                holder.add(mat[i][j]);
            }
        }
        int counter = 0;
        for(int i = 0; i < r; i++){
            for(int j = 0; j < c; j++){
                result[i][j] = holder.get(counter);
                counter++;
            }
        }
        return result;
    }
}
