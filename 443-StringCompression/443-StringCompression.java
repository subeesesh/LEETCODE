// Last updated: 5/29/2026, 11:55:34 AM
class Solution {
    public int compress(char[] chars) {
        int write = 0; 
        int read = 0; 
        while (read < chars.length) {
            char current = chars[read];
            int count = 0;
            while (read < chars.length && chars[read] == current) {
                read++;
                count++;
            }
            chars[write++] = current;
            if (count > 1) {
                String cntStr = Integer.toString(count);
                for (char c : cntStr.toCharArray()) {
                    chars[write++] = c;
                }
            }
        }
        return write;
    }
}