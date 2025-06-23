package RemoveLeaves;
import java.util.*;
public class RemoveLeaves {
    private static class Node {
        int data;
        ArrayList<Node> children = new ArrayList<>();

        Node() {
        };

        Node(int data) {
            this.data = data;
        }

        Node(int data, ArrayList<Node> children) {
            this.data = data;
            this.children = children;
        }
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
        for (Node children : root.children.reversed()) {
            System.out.println(children.data);
        }
        
        System.out.println("Original Tree:");
        displayTree(root, 0);
        
        root = removeLeaves(root);
        
        System.out.println("\nTree after removing leaves:");
        displayTree(root, 0);
    }

    private static Node removeLeaves(Node root) {
        if(root == null) return null;
        if(root.children.size() == 0) return null; // Remove leaf nodes
        
        // Remove leaves from children first
        root.children.removeIf(child -> child.children.size() == 0);
        
        // Recursively remove leaves from remaining children
        for(int i = 0; i < root.children.size(); i++) {
            root.children.set(i, removeLeaves(root.children.get(i)));
        }
        
        return root;
    }

    private static void displayTree(Node root, int level) {
        if (root == null) return;

        for (Node children : root.children) {
            displayTree(children, level + 1);
        }

        System.out.println(" ".repeat(level * 4) + root.data);
    }

}
