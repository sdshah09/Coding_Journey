'''
347. Top K Frequent Elements
Solved
Medium
Topics
Companies
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.


'''

# Time Complexity:- O(nlogk)
# Space Complexity:- O(n+k)

from typing import List
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i]=0
            freq[i]+=1
        minHeap = []
        for i,j in freq.items():
            heapq.heappush(minHeap,(j,i))
            if len(minHeap)>k:
                heapq.heappop(minHeap)
        res = []
        while minHeap:
            i,j = heapq.heappop(minHeap)
            res.append(j)
        return res