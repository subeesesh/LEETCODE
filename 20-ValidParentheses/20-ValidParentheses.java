// Last updated: 5/29/2026, 12:01:04 PM
class Solution {
    public boolean isValid(String s) {
        Stack <Character> stack=new Stack<>();
        for(char ch:s.toCharArray()){
            if(ch=='('||ch=='{'||ch=='['){
                stack.push(ch);
            }
            else if (ch==')'||ch=='}'||ch==']'){
                if (stack.isEmpty()||((ch==')'&&stack.pop()!='(')||(ch=='}'&&stack.pop()!='{')||(ch==']'&&stack.pop()!='['))){
                    return false;
                }
            }
        }
        return stack.isEmpty();
    }
}