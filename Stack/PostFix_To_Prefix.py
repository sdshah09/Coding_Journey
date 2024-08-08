'''
Postfix to Prefix Conversion
Difficulty: MediumAccuracy: 81.15%Submissions: 9K+Points: 4
You are given a string that represents the postfix form of a valid mathematical expression. Convert it to its prefix form.

Example 1:

Input: 
ABC/-AK/L-*
Output: 
*-A/BC-/AKL
Explanation: 
The above output is its valid prefix form.

Example 2:

Input: 
ab+
Output: 
+ab
Explanation: 
The above output is its valid prefix form.
Your Task:

Complete the function string postToPre(string post_exp), which takes a postfix string as input and returns its prefix form.

Expected Time Complexity: O(post_exp.length()).

Expected Auxiliary Space: O(post_exp.length()).

Constraints:

3<=post_exp.length()<=16000

post to pre is operator + t2 + +t1
'''
class Solution:
    def postToPre(self, post_exp):
        # Code here
        stack = []
        for i in post_exp:
            if i.isalnum():
                stack.append(i)
            else:
                t1 = stack.pop()
                t2 = stack.pop()
                stack.append(i+t2+t1)
        return stack[-1]
