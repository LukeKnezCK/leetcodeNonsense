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
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        if(root == null) return result;
        List<TreeNode> children = new ArrayList<>();
        if(root.left != null) children.add(root.left);
        if(root.right != null) children.add(root.right);
        result.addAll(lobHelper(children));
        ArrayList<Integer> rootArray = new ArrayList<>();
        rootArray.add(root.val);
        result.add(rootArray);
        return result;
    }
    private List<List<Integer>> lobHelper(List<TreeNode> nodes){
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        if(nodes.isEmpty()) return result;
        List<TreeNode> children = new ArrayList<>();
        List<Integer> vals = new ArrayList<>();
        for(int i = 0; i < nodes.size(); i++){
            TreeNode root = nodes.get(i);
            if(root.left != null) children.add(root.left);
            if(root.right != null) children.add(root.right);
            vals.add(root.val);
        }
        result.addAll(lobHelper(children));
        result.add(vals);
        return result;
    }
}