// Last updated: 5/29/2026, 11:52:06 AM
class Solution {
    public int smallestEvenMultiple(int n) {
        if(n%2==0){
            return n;
        }
        return 2*n;
    }
}