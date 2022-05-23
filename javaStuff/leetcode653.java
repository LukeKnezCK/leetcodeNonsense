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
    public boolean findTarget(TreeNode root, int k) {
        LinkedList<TreeNode> layer = new LinkedList<>();
        layer.add(root);
        Set<Integer> encounters = new HashSet<>();
        while(layer.size() > 0){
            int count = layer.size();
            for(int i = 0; i < count; i++){
                TreeNode currentNode = layer.removeFirst();
                if(encounters.contains(k-currentNode.val)) return true;
                else encounters.add(currentNode.val);
                if(currentNode.left != null)layer.add(currentNode.left);
                if(currentNode.right != null)layer.add(currentNode.right);
            }
        }
        return false;
    }
}