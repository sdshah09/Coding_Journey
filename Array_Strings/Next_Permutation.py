'''
31. Next Permutation
Solved
Medium
Topics
Companies
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100

'''

from typing import List

def nextGreaterPermutation(nums: List[int]) -> List[int]:
    n = len(nums)
    index = -1
    for i in range(n-2,-1,-1): # Starting from 2 indexes to compare last dip
        if nums[i]<nums[i+1]: # Found the dip
            index = i 
            break
    if index == -1: # There is no dip meaning that is the last permutation so reverse it
        nums[:] = nums[::-1]
    else:
        for i in range(n-1,index,-1): # Find the next smallest number which is most close to pivot index
            if nums[i]>nums[index]:
                nums[i],nums[index] = nums[index],nums[i]
                break
        nums[index+1:] = reversed(nums[index+1:])

if __name__ == "__main__":
    A = [2, 1, 5, 4, 3, 0, 0]
    ans = nextGreaterPermutation(A)

    print("The next permutation is: [", end="")
    for it in ans:
        print(it, end=" ")
    print("]")

