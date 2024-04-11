'''

Problem 145 (Easy) Acceptance Rate 70.8%
Given the root of a binary tree, return the postorder traversal of its nodes' values.

Example 1:

Input: root = [1,null,2,3]
Output: [3,2,1]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
 

Constraints:

The number of the nodes in the tree is in the range [0, 100].
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
        self.recurse(root.left,arr)
        self.recurse(root.right,arr)
        arr.append(root.val)

    def traversal(self,root):
        res,stack  = [],[root]
        visited = [False]
        while stack:
            cur,visit = stack.pop(),visited.pop()
            if cur:
                if visit:
                    res.append(cur.val)
                else:
                    stack.append(cur)
                    visited.append(True)
                    stack.append(cur.right)
                    stack.append(cur.left)
                    visited.append(False)
                    visited.append(False)
        # self.postorder(root,res)
        return res
    
    def preorder(self,root):
        if root is None:
            return []
        arr = []
        self.recurse(root,arr)
        val = self.traversal(root)
        return arr,val

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
