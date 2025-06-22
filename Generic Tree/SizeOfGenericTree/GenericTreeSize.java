package SizeOfGenericTree;

import java.util.ArrayList;
import java.util.Stack;

class GenericTreeSize {
    private static class Node {
        int data;
        ArrayList<Node> children = new ArrayList<>();   
    }
    
    public static void main(String[] args) {
        int[] arr = {10, 20, 50, -1, 60, -1, -1, 30, 70, -1, 80, 110, -1, 120, -1, -1, 90, -1, -1, 40};

        Stack<Node> stack = new Stack<>();
        Node root = null;
        for(int i = 0; i < arr.length; i++) {
            if(arr[i] == -1) {
                stack.pop();
            }
            else{
                Node t = new Node();
                t.data = arr[i];
                if(stack.size() > 0) {
                    stack.peek().children.add(t);
                }
                else {
                    root = t;
                }
                stack.push(t);
            }
        }
        
        // Display the tree
        System.out.println("Generic Tree Structure:");
        displayTree(root, 0);
        
        // Calculate and display size
        int size = sizeOfTree(root);
        System.out.println("\nSize of the tree: " + size);
    }
    
    private static int sizeOfTree(Node root) {
        if(root == null) return 0;
        
        int count = 1; // Count current node
        for(Node child: root.children) {
            count += sizeOfTree(child); // Add size of each subtree
        }
        return count;
    }
    
    private static void displayTree(Node node, int level) {
        if (node == null) return;
        
        // Print indentation
        for (int i = 0; i < level; i++) {
            System.out.print("  ");
        }
        
        // Print current node
        System.out.println("├─ " + node.data);
        
        // Print children
        for (int i = 0; i < node.children.size(); i++) {
            Node child = node.children.get(i);
            if (i == node.children.size() - 1) {
                // Last child
                for (int j = 0; j < level; j++) {
                    System.out.print("  ");
                }
                System.out.print("└─ ");
                displayTree(child, level + 1);
            } else {
                displayTree(child, level + 1);
            }
        }
    }
}