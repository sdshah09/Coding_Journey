'''
410. Split Array Largest Sum
Solved
Hard
Topics
Companies
Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.

Return the minimized largest sum of the split.

A subarray is a contiguous part of the array.

 

Example 1:

Input: nums = [7,2,5,10,8], k = 2
Output: 18
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.
Example 2:

Input: nums = [1,2,3,4,5], k = 2
Output: 9
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [1,2,3] and [4,5], where the largest sum among the two subarrays is only 9.
 

Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 106
1 <= k <= min(50, nums.length)

Approach:- This is a binary search problem. We have to find the maximum sum in a way that is minimum amongst all the maximum sum
Eg:-  71,73,78,79 are four of the maximum sum I have to choose 71

This problem is also similar to Books Allocation (Hard) not given in leetcode

'''
# Time Complexity:- O(log(sum(nums)-max(nums))*N)
# Space Complexity:- O(1)

from typing import List
class Solution:

    def canWeSplit(self,nums,k,size):
        total=0
        count = 1
        for i in range(len(nums)):
            if total+nums[i]>size:
                count+=1
                total = nums[i]
            else:
                total+=nums[i]
        return count

    def splitArray(self, nums: List[int], k: int) -> int:
        l,h = max(nums),sum(nums)
        while l<=h:
            mid = (l+h)//2
            if self.canWeSplit(nums,k,mid)>k:
                l = mid+1
            else:
                h=mid-1
        return l