package LinearizeTree;
import java.util.*;
public class LinearizeTree {
    static Node prev;
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

        root = linearizeTree(root);

        System.out.println("\nLinearized Tree:");
        displayTree(root, 0);

        // System.out.println("Original Tree:");
        // displayTree(root, 0);

        // root = removeLeaves(root);

        // System.out.println("\nTree after removing leaves:");
        // displayTree(root, 0);

    }

    private static Node linearizeTree(Node root) {
        if(root.children.size() == 0)
            return root;
        Node lkt = linearizeTree(root.children.get(root.children.size() - 1));
        while(root.children.size() > 1) {
            Node last = root.children.remove(root.children.size() - 1);
            Node secondLast = root.children.get(root.children.size() - 1);
            Node secondLastKeyTake = linearizeTree(secondLast);
            secondLastKeyTake.children.add(last);
        }
        return lkt;
    }

    private static void displayTree(Node node, int level) {
        if (node == null) return;
        
        // Print current node with indentation
        for (int i = 0; i < level; i++) {
            System.out.print("  ");
        }
        System.out.println("├─ " + node.data);
        
        // Print all children
        for (int i = 0; i < node.children.size(); i++) {
            Node child = node.children.get(i);
            displayTree(child, level + 1);
        }
    }

}
