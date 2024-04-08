""" 
Problem 47 (Medium)
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10

"""

'''
Solution

This is a backtracking problem. Approach, We will take a set which will add the indexes of the elements.
Why set? Because we do not want to add the elements of same index to the existing list.
So adding the indexes in set then running adding that index in list. 

Termination Condition?
Whenver the length of list == length of nums we will add that list into another list and return and start the iteration from next index

'''

class Solution:
    def __init__(self):
        pass
    def recurse(self,cur,res,nums):
        if len(cur)==len(nums):
            res.add(tuple(nums[i] for i in cur)) # Why tuple because tuple is hashable and list in unhashable
            return
        for i in range(len(nums)):
            if i not in cur:
                cur.append(i)
                self.recurse(cur,res,nums)
                cur.pop()
    def permuteUnique(self,nums):
        cur,res = [],set()
        self.recurse(cur,res,nums)
        return res
    
if __name__ == "__main__":
    sol = Solution()
    res = sol.permuteUnique([1,1,2])
    print(list(res))