// Last updated: 5/29/2026, 11:54:23 AM
class Solution {
    public boolean rotateString(String s, String goal) {
        String str=s+s;
        if ((s.length() == goal.length()) && (s + s).contains(goal)) {
    return true;
}
return false;

    }
}