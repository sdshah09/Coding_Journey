'''
Prefix to Postfix Conversion
Difficulty: MediumAccuracy: 79.97%Submissions: 10K+Points: 4
You are given a string that represents the prefix form of a valid mathematical expression. Convert it to its postfix form.

Example:

Input: 
*-A/BC-/AKL
Output: 
ABC/-AK/L-*
Explanation: 
The above output is its valid postfix form.
Your Task:

Complete the function preToPost(string pre_exp), which takes a prefix string as input and returns its postfix form.

 

Expected Time Complexity: O(N).

Expected Auxiliary Space: O(N).

Constraints:

3<=pre_exp.length()<=100

 

prefix to postfix = t1 + t2 + operator
'''

class Solution:
    def preToPost(self, pre_exp):
        stack = []
        for i in pre_exp[::-1]:
            if i.isalnum():
                stack.append(i)
            else:
                t1 = stack.pop()
                t2 = stack.pop()
                stack.append(t1+t2+i)
        return stack[-1]