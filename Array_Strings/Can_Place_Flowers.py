'''
605. Can Place Flowers
Solved
Easy
Topics
Companies
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
 

Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
Seen this question in a real interview before?
1/5
Yes
No
Accepted
810.4K
Submissions
2.8M
Acceptance Rate
29.1%

'''
from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        x = len(flowerbed)
        for i in range(x):
            if flowerbed[i]==0:
                prev = (i==0) or (flowerbed[i-1]==0)
                nextvalue = (i==x-1) or (flowerbed[i+1]==0)
                if prev and nextvalue:
                    flowerbed[i]=1
                    n-=1
                if n<=0:
                    return True
        return n<=0