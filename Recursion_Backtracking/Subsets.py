'''
Problem 78 (Medium)

Given an integer array nums of unique elements, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.

Solution.

This is a similar question to Permutations backtracking.

'''
class Solution:
    def __init__(self):
        pass
    def recurse(self,res,nums,cur,idx):
        # if len(nums)==len(cur):
        #     res.append(cur[:])
        #     return
        for i in range(idx,len(nums)):
            cur.append(nums[i])
            res.append(cur[:])
            self.recurse(res,nums,cur,i+1)
            cur.pop()
        return
    def subsets(self,nums):
        res,cur = [],[]
        res.append(cur)
        idx = 0
        self.recurse(res,nums,cur,idx)
        return res
if __name__ == "__main__":
    sol = Solution()
    res = sol.subsets([1,2,3])
    print(res)