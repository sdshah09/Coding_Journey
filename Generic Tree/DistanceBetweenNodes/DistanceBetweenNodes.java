package DistanceBetweenNodes;

import java.util.*;

public class DistanceBetweenNodes {
    private static class Node {
        int data;
        ArrayList<Node> children = new ArrayList<>();

        Node() {}

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

        // Test distance between different nodes
        System.out.println("Distance between 50 and 40: " + findDistance(root, 50, 40));
        System.out.println("Distance between 110 and 120: " + findDistance(root, 110, 120));
        System.out.println("Distance between 70 and 90: " + findDistance(root, 70, 90));
    }

    private static int findDistance(Node root, int node1, int node2) {
        // Get paths from root to both nodes
        ArrayList<Integer> path1 = nodeToRootPath(root, node1);
        ArrayList<Integer> path2 = nodeToRootPath(root, node2);
        
        if (path1.isEmpty() || path2.isEmpty()) {
            return -1; // One or both nodes not found
        }
        
        // Start from the end and iterate backwards
        int i = path1.size() - 1;
        int j = path2.size() - 1;
        
        // Keep going while both paths have the same value
        while (i >= 0 && j >= 0 && path1.get(i).equals(path2.get(j))) {
            i--;
            j--;
        }
        
        // Return i + j (distance from divergence point to both nodes)
        return i + j + 2;
    }

    private static ArrayList<Integer> nodeToRootPath(Node root, int data) {
        if (root == null) {
            return new ArrayList<>();
        }
        if (root.data == data) {
            ArrayList<Integer> path = new ArrayList<>();
            path.add(root.data);
            return path;
        }
        for (Node child : root.children) {
            ArrayList<Integer> result = nodeToRootPath(child, data);
            if (result.size() > 0) {
                result.add(0, root.data); // Add current node at beginning
                return result;
            }
        }
        return new ArrayList<>();
    }
}
