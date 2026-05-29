// Last updated: 5/29/2026, 11:59:45 AM
public class Solution {
    static ArrayList<Integer> dp = new ArrayList<>();

    public int climbStairs(int n) {
        if (n == 1) {
            return 1;
        }
        if (dp.isEmpty()) {
            dp.add(0, 0); 
            dp.add(1, 1); 
            dp.add(2, 2); 
        }
        if (n < dp.size()) {
            return dp.get(n);
        }
        for (int i = dp.size(); i <= n; i++) {
            dp.add(dp.get(i - 1) + dp.get(i - 2));
        }

        return dp.get(n);
    }
}