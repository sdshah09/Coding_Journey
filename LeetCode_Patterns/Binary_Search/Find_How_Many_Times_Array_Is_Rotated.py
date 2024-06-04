'''
Find how many times the array is rotated

THis is the same problem like find the minimum in rotated sorted array

If we find the minimum value of the array in rotated sorted array we can know the index and from the index we can say that how many times the array is rotated

'''

# Time Complexity:- O(logn)
# Space Complexity:- O(1)
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,h = 0,len(nums)-1
        while l<=h:
            mid = (l+h)//2
            if nums[mid]<nums[h]:
                h = mid
            elif nums[mid]<nums[l]:
                l = mid
            elif nums[l]<nums[h]:
                h = mid-1
            else:
                l = mid+1
        return mid