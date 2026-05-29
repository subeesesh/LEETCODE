// Last updated: 5/29/2026, 11:57:24 AM
import java.util.Arrays;
class Solution {
    public int countPrimes(int n) {
        if(n==0||n==1){
            return 0;
        }
        else{
            boolean[] isprime= new boolean[n];
            for (int i=0;i<n;i++) {
                isprime[i] = true;
            }
            isprime[0]=false;
            isprime[1]=false;
            for(int i=2;i*i<n;i++){
                if(isprime[i]){
                    for(int j=i*i;j<n;j=j+i){
                        isprime[j]=false;
                    }
                }
            }
            int count=0;
            for(int i=0;i<n;i++){
                if(isprime[i])
                count++;
            }
            return count;
        }
    }
}