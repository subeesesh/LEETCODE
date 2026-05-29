// Last updated: 5/29/2026, 11:54:57 AM
class Solution {
    public boolean checkInclusion(String s1, String s2) {
        if (s1.length() > s2.length()) return false;

        HashMap<Character, Integer> s1Count = new HashMap<>();
        for (char c : s1.toCharArray()) {
            s1Count.put(c, s1Count.getOrDefault(c, 0) + 1);
        }

        HashMap<Character, Integer> windowCount = new HashMap<>();
        int windowSize = s1.length();

        // Initial window
        for (int i = 0; i < windowSize; i++) {
            char c = s2.charAt(i);
            windowCount.put(c, windowCount.getOrDefault(c, 0) + 1);
        }

        if (s1Count.equals(windowCount)) return true;

        // Slide the window
        for (int i = windowSize; i < s2.length(); i++) {
            char newChar = s2.charAt(i);
            char oldChar = s2.charAt(i - windowSize);

            // Add new char
            windowCount.put(newChar, windowCount.getOrDefault(newChar, 0) + 1);

            // Remove old char
            windowCount.put(oldChar, windowCount.get(oldChar) - 1);
            if (windowCount.get(oldChar) == 0) {
                windowCount.remove(oldChar);
            }

            if (s1Count.equals(windowCount)) return true;
        }

        return false;
    }

}