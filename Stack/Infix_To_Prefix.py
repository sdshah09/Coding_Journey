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
    def __init__(self):
        self.stack = []
        self.output = []

    def isOperator(self, c):
        return not c.isalnum()

    def getPriority(self, C):
        if C == '-' or C == '+':
            return 1
        elif C == '*' or C == '/':
            return 2
        elif C == '^':
            return 3
        return 0

    def infixToPostfix(self, infix):
        # Add '(' to the beginning and ')' to the end of the infix expression
        infix = '(' + infix + ')'
        l = len(infix)
        stack = []
        output = ''

        for i in range(l):
            if infix[i].isalnum():
                output += infix[i]
            elif infix[i] == '(':
                stack.append('(')
            elif infix[i] == ')':
                while stack and stack[-1] != '(':
                    output += stack.pop()
                stack.pop()  # Remove '(' from the stack
            else:
                if self.isOperator(stack[-1] if stack else ''):
                    if infix[i] == '^':
                        while stack and self.getPriority(infix[i]) <= self.getPriority(stack[-1]):
                            output += stack.pop()
                    else:
                        while stack and self.getPriority(infix[i]) < self.getPriority(stack[-1]):
                            output += stack.pop()
                stack.append(infix[i])

        while stack:
            output += stack.pop()

        return output

    def infixToPrefix(self, infix):
        # Step 1: Reverse the infix expression
        infix = infix[::-1]

        # Step 2: Replace '(' with ')' and vice versa
        infix = ''.join(')' if ch == '(' else '(' if ch == ')' else ch for ch in infix)

        # Step 3: Convert the modified infix expression to postfix
        postfix = self.infixToPostfix(infix)

        # Step 4: Reverse the postfix expression to get the prefix expression
        prefix = postfix[::-1]
        return prefix

# Example usage
sol = Solution()
print("Infix expression: (p+q)*(c-d)")
print("Prefix Expression:", sol.infixToPrefix("(p+q)*(c-d)"))
