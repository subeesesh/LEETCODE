// Last updated: 5/29/2026, 11:52:07 AM
class Solution {
    public int pivotInteger(int n) {
        int sum=0;
        for(int i=1;i<=n;i++){
            sum=sum+i;
        }
        int su=0;
        for(int i=n;i>0;i--){
            su=su+i;
            if(sum==su){
                return i;
            }
            sum=sum-i;

        }
        return -1;
    }
}