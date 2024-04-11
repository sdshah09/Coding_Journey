'''
Problem 46 (Medium)

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
 

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.

Solution:- This is a backtracking problem. We will check each element if it is present in our new list and if it creates a permutation we will add it and
then pop one by one so that we can give chance to the another permutation
'''
class Solution:
    def __init__(self) -> None:
        pass
    def permutation(self,nums):
        res,cur = [],[]
        val = []
        self.recurse(nums,res,cur,val)
        return res
    def recurse(self,nums,res,cur,val):
        if len(cur) == len(nums):
            res.append(cur[:])
            return
        
        for i in range(len(nums)):
            if nums[i] not in cur:
                cur.append(nums[i])
                self.recurse(nums,res,cur,val)
                cur.pop()
        # return res
if __name__ == "__main__":
    sol = Solution()
    print(sol.permutation([1]))
