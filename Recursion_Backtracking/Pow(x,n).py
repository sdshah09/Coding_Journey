'''
50. Pow(x, n)
Solved
Medium
Topics
Companies
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

 

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
 

Constraints:

-100.0 < x < 100.0
-231 <= n <= 231-1
n is an integer.
Either x is not zero or n > 0.
-104 <= xn <= 104
Seen this question in a real interview before?
1/5
Yes
No
Accepted
1.7M
Submissions
4.8M
Acceptance Rate
34.9%


'''
# Time Complexity:- O(logn)
# Space Complexity:- O(logn)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        N = n
        if N<0:
            N = -N
            x = 1/x
        if(N%2==0):
            return self.myPow(x*x,N//2)
        else:
            return x*self.myPow(x,(N-1))
