package Traversal.ZigZagLevel;
import java.util.*;
class ZigZagLevel {
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
        System.out.println("ZigZag Level Order Traversal:");
        zigzagTraversal(root);
    }
    
    private static void zigzagTraversal(Node root) {
        Queue<Node> queue = new LinkedList<>();
        queue.offer(root);
        int level = 0;
        while(!queue.isEmpty()) {
            int n = queue.size();
            List<Integer> temp = new ArrayList<>();
            for(int i = 0; i < n; i++) {
                Node node = queue.poll();
                temp.add(node.data);
                for(Node children: node.children) {
                    queue.offer(children);
                }
            }
            
            if(level % 2 != 0) {
                Collections.reverse(temp);
            }
            
            // Print using Arrays.stream (convert List to array first)
            System.out.print("Level " + level + ": ");
            Arrays.stream(temp.toArray())
                  .forEach(node -> System.out.print(node + " "));
            System.out.println();
            
            level++;
        }
    }
   
}