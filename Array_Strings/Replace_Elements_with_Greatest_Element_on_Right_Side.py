'''
1299. Replace Elements with Greatest Element on Right Side
Solved
Easy
Topics
Companies
Hint
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.

 

Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
Explanation: 
- index 0 --> the greatest element to the right of index 0 is index 1 (18).
- index 1 --> the greatest element to the right of index 1 is index 4 (6).
- index 2 --> the greatest element to the right of index 2 is index 4 (6).
- index 3 --> the greatest element to the right of index 3 is index 4 (6).
- index 4 --> the greatest element to the right of index 4 is index 5 (1).
- index 5 --> there are no elements to the right of index 5, so we put -1.
Example 2:

Input: arr = [400]
Output: [-1]
Explanation: There are no elements to the right of index 0.
 

Constraints:

1 <= arr.length <= 104
1 <= arr[i] <= 105

# This is a similar concept to monotnic stack
'''

# Time complexity:- O(n)
# Space Complexity:- O(n)

from typing import List
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = []
        for i in range(len(arr), 0, -1):
            if len(res) == 0:
                res.append(-1)
                continue
            if arr[i] > res[-1]:
                res.append(arr[i])
            else:
                res.append(res[-1])
        return res[::-1]