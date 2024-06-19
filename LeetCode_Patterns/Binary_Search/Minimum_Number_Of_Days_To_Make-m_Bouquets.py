'''
1482. Minimum Number of Days to Make m Bouquets
Solved
Medium
Topics
Companies
Hint
You are given an integer array bloomDay, an integer m and an integer k.

You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.

The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.

Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.

 

Example 1:

Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
Output: 3
Explanation: Let us see what happened in the first three days. x means flower bloomed and _ means flower did not bloom in the garden.
We need 3 bouquets each should contain 1 flower.
After day 1: [x, _, _, _, _]   // we can only make one bouquet.
After day 2: [x, _, _, _, x]   // we can only make two bouquets.
After day 3: [x, _, x, _, x]   // we can make 3 bouquets. The answer is 3.
Example 2:

Input: bloomDay = [1,10,3,10,2], m = 3, k = 2
Output: -1
Explanation: We need 3 bouquets each has 2 flowers, that means we need 6 flowers. We only have 5 flowers so it is impossible to get the needed bouquets and we return -1.
Example 3:

Input: bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3
Output: 12
Explanation: We need 2 bouquets each should have 3 flowers.
Here is the garden after the 7 and 12 days:
After day 7: [x, x, x, x, _, x, x]
We can make one bouquet of the first three flowers that bloomed. We cannot make another bouquet from the last three flowers that bloomed because they are not adjacent.
After day 12: [x, x, x, x, x, x, x]
It is obvious that we can make two bouquets in different ways.
 

Constraints:

bloomDay.length == n
1 <= n <= 105
1 <= bloomDay[i] <= 109
1 <= m <= 106
1 <= k <= n

**Approach**:- We have to count if we the array can we make m bouquets with k flowers in each bouquets. The approach is that it is fixed that the possibility of create bouquets lies between minimum number of days tp maximum number of days provided in the array. So we can take mid point using binary search and ass that value to a function which can check if it can create m bouquets within mid point days. If it cannot then we will increase the value of lower point to mid +1 so that we can go near to maximum value of the array and find out how much minimum days we can have to find out. If it is already possible we will decrease the maximum value by mid-1 so taht we can get nearer to answer
'''

from typing import List
class Solution:
    def isPossible(self,arr,m,k,day):
        count,bou = 0,0
        for i in range(len(arr)):
            if arr[i]<=day:
                count+=1
            else:
                bou+=count//k
                count = 0
        bou+=count//k
        return bou>=m

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay)<(m*k):
            return -1
        i,j = min(bloomDay),max(bloomDay)
        while i<=j:
            mid = (i+j)//2
            if self.isPossible(bloomDay,m,k,mid):
                j = mid-1
            else:
                i = mid+1
        return i