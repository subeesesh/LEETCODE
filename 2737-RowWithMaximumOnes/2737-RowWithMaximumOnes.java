// Last updated: 5/29/2026, 11:51:58 AM
class Solution {
    public int[] rowAndMaximumOnes(int[][] mat) {
        int[] output=new int[2];
        int row=mat.length;
        int col=mat[0].length;
        int count=0,max=0;
        for(int i=0;i<row;i++){
            count=0;
            for(int j=0;j<col;j++){
                if(mat[i][j]==1){
                    count++;
                }
            }
            if(count>max){
                max=count;
                output[1]=max;
                output[0]=i;
            }
        }
        return output;

    }
}