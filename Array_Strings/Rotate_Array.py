'''
189. Rotate Array
Solved
Medium
Topics
Companies
Hint
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
 

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
 

Follow up:

Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?

Approach:-  First reverse the whole array
            Second reverse the array elements from 0 to k-1 elements
            Third reverse the elements from k to n-1
            The indexes will be index = i-k-1 for every element
'''
# Time Complexity:- O(n)
# Space Complexity:- O(1)

from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        nums[:] = nums[::-1]
        k = k%n
        l,r = 0,k-1
        while l<r:
            nums[l],nums[r] = nums[r],nums[l]
            l+=1;r-=1
        l,r = k,n-1
        while l<r:
            nums[l],nums[r] = nums[r],nums[l]
            l+=1;r-=1
        