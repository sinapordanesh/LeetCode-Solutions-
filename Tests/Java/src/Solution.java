public class Solution {
    public void gameOfLife(int[][] board) {
        for (int i = 0; i < board.length; i++){
            for (int j=0; j< board.length; j++){
                int target = board[i][j];
                int outer = i;
                int inner = j;
                int sum = 0;

                if (j == 0){
                    outer--;
                    if (outer >= 0){
                        for (int k = 0; k <= 2; k++){
                            sum += board[outer][k];
                        }
                        outer++;
                    } else
                        outer++;

                } else if (j == 1){

                } else if (j == 2){

                }


//                if (target == 1){
//
//                } else if (target == 0){
//
//                }
            }
        }
    }
}
