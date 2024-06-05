'''

540. Single Element in a Sorted Array
Solved
Medium
Topics
Companies
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.

 

Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: nums = [3,3,7,7,10,11,11]
Output: 10
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 105
Seen this question in a real interview before?
1/5
Yes
No

'''
from typing import List
class Solution:
    def singleNonDuplicate(self, arr: List[int]) -> int:
        l=0
        n=len(arr)
        h=n-1
        if n==1 : return arr[0]
        if arr[0]!=arr[1] :return arr[0]
        if arr[n-1]!=arr[n-2] :return arr[n-1]
        while(l<=h):
            m=(l+h)//2

            if(arr[m]!=arr[m+1] and arr[m-1]!=arr[m]): return arr[m]

            if(((m+1)%2)==0):
                if(arr[m]==arr[m-1]): l=m+1
                else : h=m-1
        
            else :
                if(arr[m]!=arr[m+1]) : h=m-1
                else : l=m+1
        return -1
