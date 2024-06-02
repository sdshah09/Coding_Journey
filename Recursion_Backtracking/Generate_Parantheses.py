'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]

'''

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(left,right,s):
            if len(s) == n * 2:
                res.append(s)
                return 
            if left < n:
                dfs(left + 1, right, s + '(')
            if right < left:
                dfs(left, right + 1, s + ')')

        res = []
        dfs(0, 0, '')
        return res
if __name__ == "__main__":
    sol = Solution()
    print(sol.generateParenthesis(3))
            