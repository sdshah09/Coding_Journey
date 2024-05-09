'''
Problem 144 (Easy) Acceptance Rate = 69.4%

Given the root of a binary tree, return the preorder traversal of its nodes' values.

 

Example 1:


Input: root = [1,null,2,3]
Output: [1,2,3]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 

Follow up: Recursive solution is trivial, could you do it iteratively?

'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self) -> None:
        pass
    def recurse(self,root,arr):
        if root is None:
            return arr
        arr.append(root.val)
        self.recurse(root.left,arr)
        self.recurse(root.right,arr)

    def traversal(self,root):
        res,stack = [],[]
        stack.append(root)
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right!=None:
                stack.append(node.right)
            if node.left!=None:
                stack.append(node.left)
        return res
    
    def preorder(self,root):
        if root is None:
            return []
        arr = []
        self.recurse(root,arr)
        val = self.traversal(root)
        return arr,val
    def morris(self,root):
        res = []
        cur = root
        while cur:
            if not cur.left:
                res.append(cur.val)
                cur = cur.right 
            else:
                prev = cur.left
                while prev.right and prev.right!=cur:
                    prev = prev.right
                if not prev.right:
                    res.append(cur.val)
                    prev.right = cur
                    # print(prev.right.val)
                    cur = cur.left
                else:
                    prev.right = None
                    cur = cur.right
        return res

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    print(sol.preorder(root))
