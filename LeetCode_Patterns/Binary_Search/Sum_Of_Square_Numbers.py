'''
633. Sum of Square Numbers
Solved
Medium
Topics
Companies
Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

 

Example 1:

Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5
Example 2:

Input: c = 3
Output: false
 

Constraints:

0 <= c <= 231 - 1
Seen this question in a real interview before?
1/5
Yes
No
Accepted
239.7K
Submissions
686.1K
Acceptance Rate
34.9%

'''
import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l, r = 0, int(math.sqrt(c))  # Only search up to sqrt(c)
        while l <= r:
            curSum = (l*l)+(r*r)
            if curSum == c:
                return True
            elif curSum < c:
                l+= 1
            else:
                r-=1
        return False

