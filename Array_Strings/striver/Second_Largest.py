'''
Second Largest
Difficulty: EasyAccuracy: 26.72%Submissions: 594K+Points: 2
Given an array arr, return the second largest distinct element from an array. If the second largest element doesn't exist then return -1.

Examples:

Input: arr = [12, 35, 1, 10, 34, 1]
Output: 34
Explanation: The largest element of the array is 35 and the second largest element is 34.
Input: arr = [10, 10]
Output: -1
Explanation: The largest element of the array is 10 and the second largest element does not exist so answer is -1.
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
2 ≤ arr.size() ≤ 105
1 ≤ arri ≤ 105


'''

class Solution:
    def print2largest(self, arr):
        # Code Here
        n = len(arr)
        if n<2:
            return -1
        s = f = float('-inf')
        for i in arr:
            if i>f:
                s = f
                f = i
            elif i>s and i!=f:
                s = i
        if s == float('-inf'):
            return -1
        return s