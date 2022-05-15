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
    public int deepestLeavesSum(TreeNode root) {
        ArrayList<TreeNode> nodeList = new ArrayList<>();
        ArrayList<TreeNode> nodeListAlt = new ArrayList<>();
        nodeList.add(root);
        int counter = 1;
        boolean altenator = true;
        while(altenator){
            
            for(int i = 0; i < counter; i++){
                TreeNode currentNode = nodeList.get(i);
                if(currentNode.left != null) nodeListAlt.add(currentNode.left);
                if(currentNode.right != null) nodeListAlt.add(currentNode.right);
            }
            if(nodeListAlt.size() == 0) break;
            nodeList.clear();
            counter = nodeListAlt.size();
            for(int i = 0; i < counter; i++){
                TreeNode currentNode = nodeListAlt.get(i);
                if(currentNode.left != null) nodeList.add(currentNode.left);
                if(currentNode.right != null) nodeList.add(currentNode.right);
            }
            if(nodeList.size() == 0) break;
            nodeListAlt.clear();
            counter = nodeList.size();
        }
        int result = 0;
        for(TreeNode j : nodeList) result += j.val;
        for(TreeNode j : nodeListAlt) result += j.val;
        return result;
    }
}
