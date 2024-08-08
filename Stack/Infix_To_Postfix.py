'''
Infix to Postfix
Difficulty: MediumAccuracy: 52.94%Submissions: 87K+Points: 4
Given an infix expression in the form of string str. Convert this infix expression to postfix expression.

Infix expression: The expression of the form a op b. When an operator is in-between every pair of operands.
Postfix expression: The expression of the form a b op. When an operator is followed for every pair of operands.
Note: The order of precedence is: ^ greater than * equals to / greater than + equals to -. Ignore the right associativity of ^.
Example 1:

Input: str = "a+b*(c^d-e)^(f+g*h)-i"
Output: abcd^e-fgh*+^*+i-
Explanation:
After converting the infix expression 
into postfix expression, the resultant 
expression will be abcd^e-fgh*+^*+i-
Example 2:

Input: str = "A*(B+C)/D"
Output: ABC+*D/
Explanation:
After converting the infix expression 
into postfix expression, the resultant 
expression will be ABC+*D/
 
Your Task:
This is a function problem. You only need to complete the function infixToPostfix() that takes a string(Infix Expression) as a parameter and returns a string(postfix expression). The printing is done automatically by the driver code.

Expected Time Complexity: O(|str|).
Expected Auxiliary Space: O(|str|).

Constraints:
1 ≤ |str| ≤ 105

Seen this question in a real interview before ?
Yes
No
Company Tags
PaytmVMWareMicrosoft

'''

#User function Template for python3


class Solution:
    
    def priority(self,s):
        if s == '^':
            return 3
        elif s in '*/':
            return 2
        elif s in '-+':
            return 1
        else:
            return -1
    #Function to convert an infix expression to a postfix expression.
    def InfixtoPostfix(self, exp):
        #code here
        stack = []
        s = ''
        for i in exp:
            if i.isalnum():
                s+=i
            elif i == '(':
                stack.append(i)
            elif i==')':
                while(stack and stack[-1]!="("):
                    s+=stack.pop()
                stack.pop()
            else:
                while(stack and self.priority(i)<=self.priority(stack[-1])):
                    s+=stack.pop()
                stack.append(i)
        while stack:
            s += stack.pop()
        return s

