'''
53. Maximum Subarray
Solved
Medium
Topics
Companies
Given an integer array nums, find the 
subarray
 with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.


'''
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int: # Optimal Solution
        maxSum,summ = float('-inf'),0
        for i in nums:
            summ+=i
            maxSum =max(maxSum,summ)
            if summ<0:
                summ=0
        return maxSum
    def kadanesMaximumsubArray(self,nums):
        maxSum,summ = float('-inf'),0
        start,final,end= -1,-1,-1
        for i in range(len(nums)):
            if summ == 0:
                start = i
            summ+=nums[i]
            if summ>maxSum:
                maxSum = summ
                final = start
                end = i
            if summ<0:
                summ=0
        return sum(nums[final:end+1])