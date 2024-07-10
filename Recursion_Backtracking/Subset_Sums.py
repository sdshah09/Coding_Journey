'''
Subset Sum : Sum of all Subsets


29

0
Problem Statement: Given an array print all the sum of the subset generated from it, in the increasing order.

Examples:

Example 1:

Input: N = 3, arr[] = {5,2,1}

Output: 0,1,2,3,5,6,7,8

Explanation: We have to find all the subset’s sum and print them.in this case the generated subsets are [ [], [1], [2], [2,1], [5], [5,1], [5,2]. [5,2,1],so the sums we get will be  0,1,2,3,5,6,7,8


Input: N=3,arr[]= {3,1,2}

Output: 0,1,2,3,3,4,5,6

Explanation: We have to find all the subset’s sum and print them.in this case the generated subsets are [ [], [1], [2], [2,1], [3], [3,1], [3,2]. [3,2,1],so the sums we get will be  0,1,2,3,3,4,5,6

'''

from typing import List


class Solution:
    def subsetSums(self, arr: List[int], n: int) -> List[int]:
        res = []
        def recurse(index,summ):
            if index == n:
                res.append(summ)
                return
            recurse(index+1,summ+arr[index]) # Select the current index and add it
            recurse(index+1,summ)# Do not consider the index
        recurse(0, 0)
        res.sort()
        return res

if __name__ == "__main__":
    arr = [3, 1, 2]
    ans = Solution().subsetSums(arr, len(arr))
    print("The sum of each subset is")
    for sum in ans:
        print(sum, end=" ")
    print()

