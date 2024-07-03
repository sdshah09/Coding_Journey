'''
435. Non-overlapping Intervals
Solved
Medium
Topics
Companies
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

 

Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
Example 2:

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
Example 3:

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
 

Constraints:

1 <= intervals.length <= 105
intervals[i].length == 2
-5 * 104 <= starti < endi <= 5 * 104

# Time Complexity:- O(nlogn)
# Space Complexity:- O(n)
'''
from typing import List
class Data:
    def __init__(self,start=None,end=None):
        self.start = start
        self.end = end

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        arr = [Data(intervals[i][0],intervals[i][1]) for i in range(n)]
        arr = sorted(arr,key = lambda x:x.end)
        prevEnd = arr[0].end
        count  = 0
        for i in range(1,n):
            if arr[i].start<prevEnd:
                count+=1
            else:
                prevEnd = arr[i].end
        return count