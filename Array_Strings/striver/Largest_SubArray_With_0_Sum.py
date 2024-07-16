'''
Largest subarray with 0 sum
Difficulty: MediumAccuracy: 41.84%Submissions: 304K+Points: 4
Given an array having both positive and negative integers. The task is to compute the length of the largest subarray with sum 0.

Examples:

Input: arr[] = {15,-2,2,-8,1,7,10,23}, n = 8
Output: 5
Explanation: The largest subarray with sum 0 is -2 2 -8 1 7.
Input: arr[] = {2,10,4}, n = 3
Output: 0
Explanation: There is no subarray with 0 sum.
Input: arr[] = {1, 0, -4, 3, 1, 0}, n = 6
Output: 5
Explanation: The subarray is 0 -4 3 1 0.
Expected Time Complexity: O(n).
Expected Auxiliary Space: O(n).

Constraints:
1 <= n <= 105
-1000 <= arr[i] <= 1000, for each valid i


'''

class Solution:
    def maxLen(self, n, arr):
        #Code here
        sub = {}
        curSum = 0
        k = 0
        maxLen = 0
        for i in range(n):
            curSum+=arr[i]
            if curSum==k:
                maxLen = max(maxLen,i+1)
            elif curSum in sub:
                maxLen = max(maxLen,i-sub[curSum])
            else:
                sub[curSum] = i
        return maxLen
