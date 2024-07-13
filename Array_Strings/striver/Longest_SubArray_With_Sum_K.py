'''
Longest Sub-Array with Sum K
Difficulty: MediumAccuracy: 24.64%Submissions: 314K+Points: 4
Given an array arr containing n integers and an integer k. Your task is to find the length of the longest Sub-Array with the sum of the elements equal to the given value k.

 

Examples:
 

Input :
arr[] = {10, 5, 2, 7, 1, 9}, k = 15
Output : 4
Explanation:
The sub-array is {5, 2, 7, 1}.
Input : 
arr[] = {-1, 2, 3}, k = 6
Output : 0
Explanation: 
There is no such sub-array with sum 6.
Expected Time Complexity: O(n).
Expected Auxiliary Space: O(n).

 

Constraints:
1<=n<=105
-105<=arr[i], K<=105

'''

class Solution:
    def lenOfLongSubarr (self, arr, n, k) : 
        #Complete the function
    
        prefix_sum = {}
        curr = 0
        maxLen = 0
        for i in range(n):
            curr+=arr[i]
            if curr == k:
                maxLen = max(maxLen,i+1)
            if curr-k in prefix_sum:
                maxLen = max(maxLen,i-prefix_sum[curr-k])
            if curr not in prefix_sum:
                prefix_sum[curr] = i
            
        return maxLen