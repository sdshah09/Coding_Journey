'''
875. Koko Eating Bananas
Solved
Medium
Topics
Companies
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

 

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23
 

Constraints:

1 <= piles.length <= 104
piles.length <= h <= 109
1 <= piles[i] <= 109
Seen this question in a real interview before?
1/5
Yes
No
Accepted
658K
Submissions
1.4M
Acceptance Rate
48.7%

Binary Search will be used to find the minimum number of bananas/hour 

The logic is simple. The range where the koko can eat bananas per hour would vary from 1 to the maximum value of the piles array

We have to find the minimum number of bananas/hour. So what we do it is we find the mid value of left pointer starting with 1 and right pointer starting with max value and find the mid value. We will divide the mid value with every element of the piles array and add that values. After adding that values we will check if the current speed of koko eating bananas is more or less. If she takes more hours than the hours given in the input we have to increase the speed meaning we have to move the left pointer to mid + 1 and if she has already the required speed we will decrease her eating speed to determine the minimum speed of eating her all the bananas/hour
'''

# Time Complexity:- O(N logn)
# Space Complexity:- O(1)
import math
class Solution:
    def minEatingBananas(self,piles,h):
        l,r = 1,max(piles)
        ans = r
        while l<=r:
            mid = (l+r)//2
            k = 0
            for i in piles:
                k+=math.ceil(i/mid)
            if k>h:
                l = mid+1
            else:
                ans = min(ans,k)
                r = mid-1
        return ans