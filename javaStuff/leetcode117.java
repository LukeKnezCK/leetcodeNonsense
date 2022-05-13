/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}
    
    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};
*/

class Solution {
    public Node connect(Node root) {
        if(root == null) return root;
        Node curr = root;
        Node headPointer = new Node(0);
        Node p = headPointer;
        while(curr != null){
            if(curr.left != null){
                p.next = curr.left;
                p = p.next;
            }
            if(curr.right != null){
                p.next = curr.right;
                p = p.next;
            }
            if(curr.next != null){
                curr = curr.next;
            }
            else{
                curr = headPointer.next;
                headPointer.next = null;
                p = headPointer;
            }
        }
        return root;
    }
}