class Solution {
    public boolean isValidSudoku(char[][] board) {
        HashMap<Integer, ArrayList<Character>> columnTracker = new HashMap<>();
        columnTracker.put(0, new ArrayList<Character>());
        columnTracker.put(1, new ArrayList<Character>());
        columnTracker.put(2, new ArrayList<Character>());
        columnTracker.put(3, new ArrayList<Character>());
        columnTracker.put(4, new ArrayList<Character>());
        columnTracker.put(5, new ArrayList<Character>());
        columnTracker.put(6, new ArrayList<Character>());
        columnTracker.put(7, new ArrayList<Character>());
        columnTracker.put(8, new ArrayList<Character>());
        
        HashMap<String, ArrayList<Character>> subBoxTracker = new HashMap<>();
        subBoxTracker.put("00", new ArrayList<Character>());
        subBoxTracker.put("03", new ArrayList<Character>());
        subBoxTracker.put("06", new ArrayList<Character>());
        subBoxTracker.put("30", new ArrayList<Character>());
        subBoxTracker.put("33", new ArrayList<Character>());
        subBoxTracker.put("36", new ArrayList<Character>());
        subBoxTracker.put("60", new ArrayList<Character>());
        subBoxTracker.put("63", new ArrayList<Character>());
        subBoxTracker.put("66", new ArrayList<Character>());
        
        ArrayList<Character> rowTracker = new ArrayList<>();
        
        for(int i = 0; i < 9; i++){
            for(int j = 0; j < 9; j++){
                if(rowTracker.contains(board[i][j])) return false;
                else if(columnTracker.get(j).contains(board[i][j])) return false;
                else{
                    if(board[i][j] != '.'){
                        rowTracker.add(board[i][j]);
                        columnTracker.get(j).add(board[i][j]);
                    }
                }
            }
            rowTracker.clear();
        }
        
        for(int i = 0; i < 9; i += 3){
            for(int j = 0; j < 9; j += 3){
                String box = Integer.toString(i) + Integer.toString(j);
                for(int l = i; l < i+3; l++){
                    for(int k = j; k < j+3; k++){
                        if(subBoxTracker.get(box).contains(board[l][k])) return false;
                        else{
                            if(board[l][k] != '.') subBoxTracker.get(box).add(board[l][k]);
                        }
                    }
                }
            }
        }
        
        return true;
    }
}