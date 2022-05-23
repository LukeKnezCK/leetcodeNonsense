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
    public boolean isValidBST(TreeNode root) {
        return validHelper(Long.MIN_VALUE, root, Long.MAX_VALUE );
    }
    private boolean validHelper(long min, TreeNode root, long max){
        if(root == null) return true;
        if(root.val <= min || root.val >= max) return false;
        return validHelper(min, root.left, root.val) && validHelper(root.val,root.right,max);
    }
}