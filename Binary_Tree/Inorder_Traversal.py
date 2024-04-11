'''

Problem 94(Easy)

Given the root of a binary tree, return the inorder traversal of its nodes' values.


Example 1:


Input: root = [1,null,2,3]
Output: [1,3,2]
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
    def inorderrecurse(self,root,arr):
        if root is None:
            return
        self.inorderrecurse(root.left,arr)
        arr.append(root.val)
        self.inorderrecurse(root.right,arr)

    def traverse_inorder(self,root):
        res,stack = [],[]
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur =cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res
    def inordertraversal(self,root):
        arr = []
        self.inorderrecurse(root,arr)
        res = self.traverse_inorder(root)
        return arr,res

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    solution = Solution()
    print(solution.inordertraversal(root))  
