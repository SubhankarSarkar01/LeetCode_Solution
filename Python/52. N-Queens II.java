// ---- 52. N-Queens II ----
class Solution {
    public boolean isSafe(char board[][],int row,int col){
        // Vertical
        for(int i=row-1;i>=0;i--){
            if(board[i][col] == 'Q'){
                return false;
            }
        }

        // left diagonal
        for(int i=row-1,j=col-1;i>=0 && j>=0;i--,j--){
            if(board[i][j] == 'Q'){
                return false;
            }
        }

        // right diagonal
        for(int i=row-1,j=col+1;i>=0 && j<board.length;i--,j++){
            if(board[i][j] == 'Q'){
                return false;
            }
        }
        return true;

    }
    public void nQueen(char board[][],int row){
        if (row == board.length){
            count++;
            return ;
        }
        for(int j=0;j<board.length;j++){
            if(isSafe(board,row,j)){
                board[row][j] = 'Q';
                nQueen(board,row+1);
                board[row][j] = 'X';
            }
            
        }
    }
    int count =0;
    public int totalNQueens(int n) {
        char board[][] = new char[n][n];
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                board[i][j] = 'X';
            }
        }
        nQueen(board,0);
        return count;
    }
}