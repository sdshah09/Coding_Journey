'''
Problem 128 (Medium)

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109

Time Complexity:- O(N)
Space Complexity:- O(N)

'''
from typing import List
class Solution:
    def __init__(self) -> None:
        pass
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_val = 0
        end = 0
        for i in nums:
            if i-1 not in nums:
                end = i+1
                while end in nums:
                    end+=1
                max_val = max(max_val,end-i)
        return max_val

if __name__ == "__main__":
    sol = Solution()
    print(sol.longestConsecutive([100,4,200,1,3,2]))
