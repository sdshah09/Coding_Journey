'''
20. Valid Parentheses
Solved
Easy
Topics
Companies
Hint
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

'''

class Solution:
    def isValid(self, s: str) -> bool:
        freq = {'(':')','[':']','{':'}'}
        res = []
        for i in s:
            if i in '[({':
                res.append(i)
            elif i in freq.values():
                if res:
                    val=res.pop()
                    print(freq[val])
                    if freq[val]!=i:
                        return False
                else:
                    return False
        if res:
            return False
        return True
    def isValid2(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in "({[":
                stack.append(i)
            else:
                if stack:
                    ch = stack.pop()
                    if (i==")" and ch=="(") or (i=="]" and ch=="[") or (i=="}" and ch=="{"):
                        continue
                    else:
                        return False
                else:
                    return False

        return not stack 
            