'''
Problem 231 (Easy)

Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1
Example 2:

Input: n = 16
Output: true
Explanation: 24 = 16
Example 3:

Input: n = 3
Output: false
 

Constraints:

-231 <= n <= 231 - 1
 

Follow up: Could you solve it without loops/recursion?

Two Solutions

1. Using Recursion
Ans:- If n%2 == 0 return True if n%2==1 return False 
Divide the number everytime by 2 to check if it is power or not

2. Bit Manipulation
Ans:-  If we use and operation of current number with it's previous number and if it returns 0 it is a power or it isn't
'''

class Solution:
    def __init__(self):
        pass
    def recurse(self,nums):
        if nums==1:
            return True
        if nums%2!=0:
            print(nums)
            return False
        if nums<1:
            return False
        print(nums)
        return self.recurse(nums//2)
    def bit(self,nums):
        return nums&(nums-1)==0

if __name__ == "__main__":
    sol = Solution()
    res = sol.recurse(4096)
    print(res)