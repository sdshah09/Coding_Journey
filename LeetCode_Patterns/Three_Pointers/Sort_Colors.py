'''
75. Sort Colors
Solved
Medium
Topics
Companies
Hint
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
 

Constraints:

n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.
 

Follow up: Could you come up with a one-pass algorithm using only constant extra space?

This is a problem which is using three pointer meaning why do we need three pointers. This is also called Dutch Flag Algorithm. In two pointers we were checking only the right most pointer with the current pointer and comparing or adding the values. In this problem if we take a test case for example [1,0,2] O/P should be [0,1,2] but if we try to apply two pointers we won't get any output because the we if the zero is in middle then we need to check the next as well as the previous value and swap accordingly. So keep check of left as well as right pointer we declared a mid pointer which will work according to the condition which is provided in the problem. In this we need to sort from color red i.e. 0 so 0 should be first and that will also work for our condition so work accordingly that condition.

Confusion:- Still don't know how to manipulate the left and right pointer w.r.t mid pointer
'''
from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l,m,r = 0,0,len(nums)-1
        while m<=r:
            if nums[m]==0:
                nums[m],nums[l] = nums[l],nums[m]
                l+=1
                m+=1
            elif nums[m]==1:
                m+=1
            else:
                nums[m],nums[r] = nums[r],nums[m]
                r-=1
            
        return nums