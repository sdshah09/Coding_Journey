'''
Problem 39 (Medium)
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency
 of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []
 

Constraints:

1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40

Solution
Approach:- This is backtracking problem. We will append the candidates to a list and these candidates can be repetitive
Termination Condition if value is less than 0 then return
or val == 0 then append and return

So for example I/P = [2,3,6,7]

Sequence would be 
[2]->[2,2]-> [2,2,2] -> [2,2,2,2] < 0 return
[2]->[2,2]-> [2,2,2] -> [2,2,2,3] < 0 return
[2]->[2,2]-> [2,2,2] -> [2,2,2,6] < 0 return
[2]->[2,2]-> [2,2,2] -> [2,2,2,7] < 0 return
[2]->[2,2]-> [2,2,2] -> [2,2,3] --> append because val == 0 i.e. target achieved
[2]->[2,2]-> [2,2,2] -> [2,2,6] < 0 return
[2]->[2,2]-> [2,2,2] -> [2,2,7] < 0 return

[2]->[2,2]-> [2,2,2] -> [2,3]
[2]->[2,2]-> [2,2,2] -> [2,3,3] < 0 return
[2]->[2,2]-> [2,2,2] -> [2,6] < 0 return
[2]->[2,2]-> [2,2,2] -> [2,7] <0 return

[3] -> [3,3]
[3] -> [3,3,3] < 0 return
[3] -> [3,3,6] < 0 return
[3] -> [3,3,7] < 0 return

[3] -> [3,6] < 0 return
[3] -> [3,7] < 0 return

Same for 6 and 7

'''

class Solution:
    
    def __init__(self):
        pass
    def recurse(self,candidates,val,res,cur,idx):
        if val<0:
            return
        if val==0:
            res.append(cur[:])
            return
        for i in range(idx,len(candidates)):
            cand = candidates[i]
            cur.append(candidates[i])
            self.recurse(candidates,val-cand,res,cur,i)
            cur.pop()
    def combinationSum(self, candidates, target):
        res,cur = [],[]
        self.recurse(candidates,target,res,cur,0)
        return res

if __name__ == "__main__":
    sol = Solution()
    res = sol.combinationSum([2,3,6,7],7)
    print(res)