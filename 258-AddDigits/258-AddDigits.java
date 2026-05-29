// Last updated: 5/29/2026, 11:56:34 AM
class Solution {
    public int addDigits(int num) {
        if(num<10){
            return num;
        }
        int rem=0,sum=0;
        int temp=num;
        while(num>0){
            rem=num%10;
            sum=sum+rem;
            num=num/10;
        }
        return addDigits(sum);
    }
}