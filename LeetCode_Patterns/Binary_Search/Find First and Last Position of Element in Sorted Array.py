'''
34. Find First and Last Position of Element in Sorted Array
Solved
Medium
Topics
Companies
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109

Time Complexity: O(log n)
Space Complexity: O(1)


'''

from typing import List

class Solution:
    def firstOccur(self,nums,target):
        i,j=0,len(nums)-1
        first = -1
        while i<=j:
            mid = (i+j)//2
            if nums[mid]==target:
                first = mid
                j = mid-1
            elif nums[mid]>target:
                j = mid-1
            else:
                i = mid+1
        return first
    def lastOccur(self,nums,target):
        i,j=0,len(nums)-1
        last = -1
        while i<=j:
            mid = (i+j)//2
            if nums[mid]==target:
                last = mid
                i = mid+1
            elif nums[mid]>target:
                j = mid-1
            else:
                i = mid+1
        return last
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.firstOccur(nums,target)
        last = self.lastOccur(nums,target)
        return [first,last]

if __name__ == "__main__":
    sol = Solution()
    print(sol.searchRange([1,2,2,3,3,3,3,4,5,6,7],3))