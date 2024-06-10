'''
Sum of all elements between k1’th and k2’th smallest elements
Last Updated : 06 Apr, 2023
Given an array of integers and two numbers k1 and k2. Find the sum of all elements between given two k1’th and k2’th smallest elements of the array. It may be assumed that (1 <= k1 < k2 <= n) and all elements of array are distinct.

Examples : 

Input : arr[] = {20, 8, 22, 4, 12, 10, 14},  k1 = 3,  k2 = 6  
Output : 26          
         3rd smallest element is 10. 6th smallest element 
         is 20. Sum of all element between k1 & k2 is
         12 + 14 = 26

Input : arr[] = {10, 2, 50, 12, 48, 13}, k1 = 2, k2 = 6 
Output : 73 

'''

import Kth_Smallest_Element

class Solution:
    def func(self,arr,k1,k2):
        arr.sort()
        first = Kth_Smallest_Element.Solution.maxHeap(self,arr,k1)
        second = Kth_Smallest_Element.Solution.maxHeap(self,arr,k2)
        summ = 0
        for i in arr:
            if first<i<second:
                summ+=i
        return summ
if __name__ == "__main__":
    sol = Solution()
    print(sol.func([10, 2, 50, 12, 48, 13],2,6))