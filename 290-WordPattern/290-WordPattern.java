// Last updated: 5/29/2026, 11:56:27 AM
class Solution {
    public boolean wordPattern(String pattern, String s) {
        String[] words = s.split(" ");
        if (pattern.length() != words.length) {
            return false;
        }
        HashMap<Character, String> map = new HashMap<>();
        HashSet<String> usedWords = new HashSet<>();
        for (int i = 0; i < pattern.length(); i++) {
            char c = pattern.charAt(i);
            String word = words[i];
            if (map.containsKey(c)) {
                if (!map.get(c).equals(word)) {
                    return false;
                }
            } else {
                if (usedWords.contains(word)) {
                    return false;
                }
                map.put(c, word);
                usedWords.add(word);
            }
        }
        return true;
    }
}