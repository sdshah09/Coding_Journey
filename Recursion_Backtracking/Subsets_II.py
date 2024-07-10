'''
90. Subsets II
Solved
Medium
Topics
Companies
Given an integer array nums that may contain duplicates, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10

'''
from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set();ans = []
        n = len(nums)
        def recurse(cur,index):
            if index == n:
                res.add(tuple(cur))
                return
            cur.append(nums[index])
            recurse(cur,index+1)
            cur.pop()
            recurse(cur,index+1)
        cur = []
        nums.sort()
        recurse(cur,0)
        return res