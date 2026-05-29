// Last updated: 5/29/2026, 11:59:33 AM
class Solution {
    public int largestRectangleArea(int[] heights) {
        Stack<Integer> st = new Stack<>();
        int max = 0;

        for (int i = 0; i < heights.length; i++) {

            while (!st.isEmpty() && heights[i] < heights[st.peek()]) {
                int h = heights[st.pop()];
                int width;

                if (st.isEmpty()) {
                    width = i;
                } else {
                    width = i - st.peek() - 1;
                }

                max = Math.max(max, h * width);
            }

            st.push(i); 
        }
        int n = heights.length;
        while (!st.isEmpty()) {
            int h = heights[st.pop()];
            int width;

            if (st.isEmpty()) {
                width = n;
            } else {
                width = n - st.peek() - 1;
            }

            max = Math.max(max, h * width);
        }

        return max;
    }
}
