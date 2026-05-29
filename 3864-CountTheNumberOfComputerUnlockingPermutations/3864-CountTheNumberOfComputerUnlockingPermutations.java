// Last updated: 5/29/2026, 11:51:34 AM
class Solution {
    public int countPermutations(int[] complexity) {
        int min=complexity[0];
        long fact=1;
        long mod = 1000000007;
        for(int i=1;i<complexity.length;i++){
            if(complexity[i]<=min){
                return 0;
            }
            fact=(fact*i)%mod;
        }
        return (int)fact;
    }
}