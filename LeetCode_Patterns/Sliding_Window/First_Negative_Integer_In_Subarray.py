'''
First negative integer in every window of size k
Given an array and a positive integer k, find the first negative integer for each window(contiguous subarray) of size k. If a window does not contain a negative integer, then print 0 for that window.

Examples:  

Input : arr[] = {-8, 2, 3, -6, 10}, k = 2
Output : -8 0 -6 -6
First negative integer for each window of size k
{-8, 2} = -8
{2, 3} = 0 (does not contain a negative integer)
{3, -6} = -6
{-6, 10} = -6
Input : arr[] = {12, -1, -7, 8, -15, 30, 16, 28} , k = 3
Output : -1 -1 -7 -15 -15 0

'''

class Solution:
    def func(self,nums,k):
        i,j=0,0
        cur = []
        while j<len(nums):
            if nums[j]<0:
                cur.append(nums[j])
            if((j-i+1)==k):
                if not cur:
                    print(0)
                elif nums[i]==cur[0]:
                    print(cur[0])
                    cur.pop(0)
                i+=1
            j+=1
        return "Done"

if __name__ == "__main__":
    sol = Solution()
    print(sol.func([1,2,3,-4,-5,-6,-7],3))