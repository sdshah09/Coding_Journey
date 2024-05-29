'''

560. Subarray Sum Equals K
Solved
Medium
Topics
Companies
Hint
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107

'''

from typing import List

# Only for positive and 0 present in array T(C):- O(N) and S(C):- O(1)
def getLongestSubarray(a: List[int], k: int) -> int:
    n = len(a)
    left, right = 0, 0
    Sum = 0
    maxLen = 0
    while right < n:
        Sum += a[right]
        while left <= right and Sum > k:
            Sum -= a[left]
            left += 1
        if Sum == k:
            maxLen = max(maxLen, right - left + 1)
        right += 1

    return maxLen

# Works with negative number also T(C):- O(N) and S(C):- O(N)
def subarraySum(nums, k):
    n = len(nums)
    count = 0
    curr_sum = 0
    freq = {0: 0}  # Initialize with 0 sum occurring once
    for num in nums:
        curr_sum += num
        if curr_sum == k:
            count += 1
        if curr_sum - k in freq:
            count += freq[curr_sum - k]
        freq[curr_sum] = freq.get(curr_sum, 0) + 1

    return count



if __name__ == "__main__":
	a = [4, 1, 1, 1, 2,3,5]
	k = 4

	length = getLongestSubarray(a, k)
	print(f"The length of the longest subarray is: {length}")



