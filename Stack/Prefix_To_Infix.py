'''
Prefix to Infix Conversion
Difficulty: MediumAccuracy: 72.66%Submissions: 11K+Points: 4
You are given a string S of size N that represents the prefix form of a valid mathematical expression. Convert it to its infix form.

Example 1:

Input: 
*-A/BC-/AKL
Output: 
((A-(B/C))*((A/K)-L))
Explanation: 
The above output is its valid infix form.
Your Task:

Complete the function string preToInfix(string pre_exp), which takes a prefix string as input and return its infix form.

 

Expected Time Complexity: O(N).

Expected Auxiliary Space: O(N).

Constraints:

3<=|S|<=104

Similar to postfix to infix just reverse the string
'''
class Solution:
    def reverse_infix(self,exp):
    # Reverse the string and swap parentheses
        reversed_exp = exp[::-1]
        reversed_exp = ''.join(')' if ch == '(' else '(' if ch == ')' else ch for ch in reversed_exp)
        return reversed_exp


    def preToInfix(self, pre_exp):
        # Code here
        stack = []
        for i in pre_exp[::-1]:
            if i.isalnum():
                stack.append(i)
            else:
                t1 = stack.pop()
                t2 = stack.pop()
                stack.append("(" + t2 + i + t1 + ")")
        return self.reverse_infix(stack[-1])
