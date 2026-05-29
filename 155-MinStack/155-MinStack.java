// Last updated: 5/29/2026, 11:57:59 AM
class MinStack {
    Stack<Integer> st;
    Stack<Integer> mins;
    public MinStack() {
        st=new Stack<>();
        mins=new Stack<>();
    }
    
    public void push(int val) {
        st.push(val);
        int min=Integer.MAX_VALUE;
        if(mins.empty()){
            mins.push(val);
        }
        else {
            mins.push(Math.min(mins.peek(),val));
        }
    }
    
    public void pop() {
        st.pop();
        mins.pop();
    }
    
    public int top() {
        return st.peek();
    }
    
    public int getMin() {
        return  mins.peek();
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */