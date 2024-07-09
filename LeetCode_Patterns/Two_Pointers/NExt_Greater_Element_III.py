'''
556. Next Greater Element III
Solved
Medium
Topics
Companies
Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive integer exists, return -1.

Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 32-bit integer, return -1.

 

Example 1:

Input: n = 12
Output: 21
Example 2:

Input: n = 21
Output: -1

'''
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        index = -1
        n = list(str(n))
        x = len(n)
        for i in range(x-2,-1,-1):
            if n[i]<n[i+1]:
                index = i
                break
        if index==-1:
            return -1
        for i in range(x-1,index,-1):
            if n[i]>n[index]:
                n[i],n[index] = n[index],n[i]
                break
        n[index+1:] = reversed(n[index+1:])
        n = int(''.join(n))
        return n if n<=(2**31-1) else -1
        