'''
Given an infix expression, the task is to convert it to a prefix expression.

Infix Expression: The expression of type a ‘operator’ b (a+b, where + is an operator) i.e., when the operator is between two operands.

Prefix Expression: The expression of type ‘operator’ a b (+ab where + is an operator) i.e., when the operator is placed before the operands.

Examples: 

Input: A * B + C / D
Output: + * A B/ C D 

Input: (A – B/C) * (A/K-L)
Output: *-A/BC-/AKL

Steps
1. Reverse the string
2.  Convert the reversed string to postfix from infix
3. Again reverse the string that is your prefix answer
'''

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
                while(stack and self.priority(i)<self.priority(stack[-1])): # The only change is if the priority is same we append it to the stack rather than popping and adding to the string
                    s+=stack.pop()
                stack.append(i)
        while stack:
            s += stack.pop()
        return s

    def InfixToPrefix(self,exp):
        exp = exp[::-1]
        prefix = self.InfixtoPostfix(exp)
        return prefix[::-1]