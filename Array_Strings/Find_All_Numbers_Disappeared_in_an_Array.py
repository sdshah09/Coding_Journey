'''
448. Find All Numbers Disappeared in an Array
Solved
Easy
Topics
Companies
Hint
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]
 

Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
 

Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Same logic as First Missing Positive Number
'''
from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            nums[abs(nums[i]) - 1] = abs(nums[abs(nums[i]) - 1]) * -1
        ans = []
        for i in range(n):
            if nums[i]>0:
                ans.append(i+1)
        return ans