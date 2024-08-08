'''
You are given a string that represents the postfix form of a valid mathematical expression. Convert it to its infix form.

Example:

Input:
ab*c+ 
Output: 
((a*b)+c)
Explanation: 
The above output is its valid infix form.
Your Task:

Complete the function string postToInfix(string post_exp), which takes a postfix string as input and returns its infix form.

 

Expected Time Complexity: O(N).

Expected Auxiliary Space: O(N).

Constraints:

3<=post_exp.length()<=104

postfix to infix is ( + t2 + operator + t1  )
'''

class Solution:
    def postToInfix(self, postfix):
        # Code here
        stack = []
        for i in postfix:
            if i.isalnum():
                stack.append(i)
            else:
                t1 = stack.pop()
                t2 = stack.pop()
                st = "(" + t2 + i + t1 + ")"
                stack.append(st)
        return stack[-1]
sol = Solution()
print(sol.postToInfix("ab*c+"))