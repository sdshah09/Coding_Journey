'''
1248. Count Number of Nice Subarrays
Solved
Medium
Topics
Companies
Hint
Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.

 

Example 1:

Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
Example 2:

Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There are no odd numbers in the array.
Example 3:

Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16
 

Constraints:

1 <= nums.length <= 50000
1 <= nums[i] <= 10^5
1 <= k <= nums.length

Approach:- There are two scenarios in this code. One is even and one is odd. If our index i is on even and we have found the window of our subarray equal to value k we need to move the index i until we do not find the next odd element. There after we can go ahead and count the number of subarrays before that i. This is for even. And after that i index is on odd element we need to move the right pointer (j)

Scenario 2:- Consider your current index is already on odd element. Then when you find the subarray window you just need to increase the i by only 1 index and there after start counting with window k once again.

For this we need to manipulate value of our window i.e. k so whenever k==0 we are sure we had find out our window. So start moving index i until we don't find the next odd element.

Using that logic k+=nums[i]%2
'''

from typing import List
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        i,j = 0,0
        res,count = 0,0
        while j<len(nums):
            if nums[j]%2==1:
                k-=1
                count = 0
            while not k:
                k+=(nums[i]%2)
                i+=1
                count+=1
            res+=count
            j+=1
        return res