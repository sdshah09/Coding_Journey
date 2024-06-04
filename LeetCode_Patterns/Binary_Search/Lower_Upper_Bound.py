'''
 Implement Lower Bound
Easy
0/40
Average time to solve is 20m
Contributed by
270 upvotes
Problem statement
You are given an array 'arr' sorted in non-decreasing order and a number 'x'.

You must return the index of lower bound of 'x'.

Note:
For a sorted array 'arr', 'lower_bound' of a number 'x' is defined as the smallest index 'idx' such that the value 'arr[idx]' is not less than 'x'

If all numbers are smaller than 'x', then 'n' should be the 'lower_bound' of 'x', where 'n' is the size of array.

Consider 0-based indexing.

Example:
Input: ‘arr’ = [1, 2, 2, 3] and 'x' = 0

Output: 0

Explanation: Index '0' is the smallest index such that 'arr[0]' is not less than 'x'.

Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1:
6
1 2 2 3 3 5
0

Sample Output 1:
0

Explanation Of Sample Input 1 :
Index '0' is the smallest index such that 'arr[0]' is not less than 'x'.

Sample Input 2:
6
1 2 2 3 3 5
2


Sample Output 2:
1


Sample Input 3:
6
1 2 2 3 3 5
7


Sample Output 3:
6


Expected Time Complexity:
Try to do this in O(log(n)).


Constraints:
1 <= ‘n’ <= 10^5
0 <= ‘arr[i]’ <= 10^5
1 <= ‘x’ <= 10^5

'''

class Solution:
    def lowerBound(self,nums,x):
        l,h = 0,len(nums)-1
        ans = x
        while l<=h:
            mid = (l+h)//2
            if nums[mid]>=x: # Look at left
                ans = mid
                h = mid-1
            else: # Look at right
                l=mid+1
        return ans
    def upperBound(self,nums,x):
        l,h = 0,len(nums)-1
        ans = x
        while l<=h:
            mid = (l+h)//2
            if nums[mid]>x: # Look at left
                ans = mid
                h = mid-1
            else: # Look at right
                l=mid+1
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.lowerBound([1,3,4,5],5)) 
    print(sol.upperBound([1,3,4,5],5)) 