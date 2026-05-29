// Last updated: 5/29/2026, 11:59:14 AM
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
    //     List<Integer> result=new ArrayList<>();
    //     List<Integer> result1=new ArrayList<>();
    //     postOrder(p,result);
    //     postOrder(q,result1);
    //     if(result.equals(result1)){
    //         return true;
    //     }
    //     else {
    //         return false;
    //     }
    // }
    //     public void postOrder(TreeNode root, List<Integer> result){
    //         if (root == null)
    //         return;
    //     postOrder(root.left,result);
    //     postOrder(root.right,result);
    //     result.add(root.val);
    //     }
        if (p == null && q == null) return true;
        if (p == null || q == null) return false;

        return (p.val == q.val)
            && isSameTree(p.left, q.left)
            && isSameTree(p.right, q.right);}

}
