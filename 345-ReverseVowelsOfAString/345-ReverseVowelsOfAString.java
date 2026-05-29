// Last updated: 5/29/2026, 11:56:03 AM
class Solution {
    public String reverseVowels(String s) {
        char[] arr=s.toCharArray();
        String vowels = "aeiouAEIOU";
        char temp;
        int i=0,j=s.length()-1;
        while(i<j){
            while (vowels.indexOf(arr[i]) == -1&&i<j){
                i++;
            }
            while (vowels.indexOf(arr[j]) == -1&&i<j){
                j--;
            }
            temp=arr[i];
            arr[i]=arr[j];
            arr[j]=temp;
            i++;
            j--;
        }
        return new String(arr);
    }
}