package SearchElement;

import java.util.*;
public class SearchElement {
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
        System.out.println("Is value present:: " +  isElementPresent(root, 150));
    }

    private static boolean isElementPresent(Node root, int value) {
        if(root == null) return false;
        if(root.data == value) return true;
        for(Node children: root.children) {
            if(isElementPresent(children, value))
                return true;
        } 
        return false;
    }
}
