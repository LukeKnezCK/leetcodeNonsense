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
    private int counter = 0;
        
    public int minCameraCover(TreeNode root) {
        if(helper(root) == 0) counter++;
        return counter;
    }
    
    private int helper(TreeNode root){
        if(root == null) return 1;
        int left = helper(root.left);
        int right = helper(root.right);
        if(left == 1 && right == 1) {
            return 0;
        }
        else if(left == 0 || right == 0){
            counter++;
            return 2;
        }
        else return 1;
    }
}