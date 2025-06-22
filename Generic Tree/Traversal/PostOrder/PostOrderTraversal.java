// package Traversal.PreOrder;
// package PrePostTraversal;
import java.util.*;
public class PostOrderTraversal {
    private static class Node {
        int data;
        ArrayList<Node> children = new ArrayList<>();
    }

    public static void main(String[] args) {
        int[] arr = { 10, 20, 50, -1, 60, -1, -1, 30, 70, -1, 80, 110, -1, 120, -1, -1, 90, -1, -1, 40 };

        Stack<Node> stack = new Stack<>();
        Node root = null;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == -1) {
                stack.pop();
            } else {
                Node t = new Node();
                t.data = arr[i];
                if (stack.size() > 0) {
                    stack.peek().children.add(t);
                } else {
                    root = t;
                }
                stack.push(t);
            }
        }

        // System.out.println("Preorder Traversal\n");
        // preOrderTraversal(root);

        System.out.println("PostOrder Traversal");
        postOrderTraversal(root);

    }

    private static void postOrderTraversal(Node root) {
        if(root == null) return;
        for(Node children: root.children) {
            postOrderTraversal(children);
        }
        System.out.println("For postOrder traversal printing node: " + root.data);
    }

}
