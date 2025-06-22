package Traversal.LevelOrderLinewise;
import java.util.*;
public class LevelOrderLineWise {
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
        System.out.println("Level Order Traversal Linewise is: \n");
        levelOrderTraversalLinewise(root);
    }

    private static void levelOrderTraversalLinewise(Node root) {
        Queue<Node> queue = new LinkedList<>();
        queue.offer(root);
        while(!queue.isEmpty()) {
            int n = queue.size();
            System.out.print("Level: ");
            for(int i = 0; i < n; i++) {
                Node node = queue.poll();
                System.out.print(node.data + " ");
                for(Node children: node.children) {
                    queue.offer(children);
                }
            }
            System.out.println();
        }
    }    
}
