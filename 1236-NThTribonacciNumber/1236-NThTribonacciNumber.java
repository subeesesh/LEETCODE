// Last updated: 5/29/2026, 11:53:32 AM
import java.util.ArrayList;

public class Solution {
    static ArrayList<Integer> dp = new ArrayList<>();

    public int tribonacci(int n) {
        if (dp.isEmpty()) {
            dp.add(0); 
            dp.add(1); 
            dp.add(1); 
        }
        if (n < dp.size()) {
            return dp.get(n);
        }
        for (int i = dp.size(); i <= n; i++) {
            int val = dp.get(i - 1) + dp.get(i - 2) + dp.get(i - 3);
            dp.add(val);
        }
        return dp.get(n);
    }
}
