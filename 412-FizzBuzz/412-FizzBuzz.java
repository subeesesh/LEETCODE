// Last updated: 5/29/2026, 11:55:41 AM
class Solution {
    public List<String> fizzBuzz(int n) {
        List<String> list=new ArrayList<>();
        for(int x=1;x<=n;x++){
            if(x%3==0 && x%5==0){
                list.add("FizzBuzz");
            }
            else if(x%3==0){
                list.add("Fizz");
            }
            else if(x%5==0){
                list.add("Buzz");
            }
            else{
                list.add(String.valueOf(x));
            }
        }
        return list;
    }
}