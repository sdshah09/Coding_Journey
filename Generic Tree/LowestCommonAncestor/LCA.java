package LowestCommonAncestor;

import java.util.*;
public class LCA {
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
        // for (Node children : root.children.reversed()) {
        //     System.out.println(children.data);
        // }
        // System.out.println("Is value present:: " + nodeToRootPath(root, 150));
        
        // Create example nodes to find LCA
        Node node110 = findNode(root, 110);
        Node node120 = findNode(root, 120);
        
        if (node110 != null && node120 != null) {
            Node lca = findLCA(root, node110, node120);
            System.out.println("LCA of " + node110.data + " and " + node120.data + " is: " + lca.data);
            
            // Show paths
            ArrayList<Integer> path1 = nodeToRootPath(root, node110.data);
            ArrayList<Integer> path2 = nodeToRootPath(root, node120.data);
            System.out.println("Path to " + node110.data + ": " + path1);
            System.out.println("Path to " + node120.data + ": " + path2);
        }
        
        // Another example
        Node node50 = findNode(root, 50);
        Node node60 = findNode(root, 40);
        
        if (node50 != null && node60 != null) {
            Node lca2 = findLCA(root, node50, node60);
            System.out.println("LCA of " + node50.data + " and " + node60.data + " is: " + lca2.data);
            
            // Show paths
            ArrayList<Integer> path1 = nodeToRootPath(root, node50.data);
            ArrayList<Integer> path2 = nodeToRootPath(root, node60.data);
            System.out.println("Path to " + node50.data + ": " + path1);
            System.out.println("Path to " + node60.data + ": " + path2);
            
            // Test iterative approach
            Node lcaIterative = findLCAIterative(root, node50, node60);
            System.out.println("Iterative LCA: " + lcaIterative.data);
        }
    }

    private static Node findLCA(Node root, Node p, Node q) {
        if(root == null || root == p || root == q) {
            return root;
        }
        
        Node found = null;
        for(Node child: root.children) {
            Node result = findLCA(child, p, q);
            if(result != null) {
                if(found == null) {
                    found = result;
                } else {
                    return root;
                }
            }
        }
        return found;
    }

    private static Node findNode(Node root, int data) {
        if (root == null) {
            return null;
        }
        if (root.data == data) {
            return root;
        }
        for (Node child : root.children) {
            Node result = findNode(child, data);
            if (result != null) {
                return result;
            }
        }
        return null;
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
                result.add(root.data);
                return result;
            }
        }
        return new ArrayList<>();
    }

    private static Node findLCAIterative(Node root, Node p, Node q) {
        // Get paths from root to both nodes
        ArrayList<Integer> path1 = nodeToRootPath(root, p.data);
        ArrayList<Integer> path2 = nodeToRootPath(root, q.data);
        
        if (path1.isEmpty() || path2.isEmpty()) {
            return null; // One or both nodes not found
        }
        
        // Start from the end (closest to root) and iterate backwards
        int i = path1.size() - 1;
        int j = path2.size() - 1;
        
        // Keep going while both paths have the same value
        while (i >= 0 && j >= 0 && path1.get(i).equals(path2.get(j))) {
            i--;
            j--;
        }
        
        // The LCA is the node after the last common node
        // So we need to go back one step
        if (i + 1 < path1.size()) {
            return findNode(root, path1.get(i + 1));
        }
        
        return null;
    }
}
