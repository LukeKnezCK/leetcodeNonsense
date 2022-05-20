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
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        if(root == null)return result;
        Queue<TreeNode> layer = new LinkedList<>();
        layer.add(root);
        while(layer.size() > 0){
            int counter = layer.size();
            List<Integer> layerContents = new ArrayList<>();
            for(int i = 0; i < counter; i++){
                TreeNode currentNode = layer.remove();
                layerContents.add(currentNode.val);
                if(currentNode.left != null) layer.add(currentNode.left);
                if(currentNode.right != null) layer.add(currentNode.right);
            }
            result.add(layerContents);
        }
        return result;
    }
}