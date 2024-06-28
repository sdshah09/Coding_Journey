'''
Problem 77 (Medium)
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

 

Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
Example 2:

Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.
 

Constraints:

1 <= n <= 20
1 <= k <= n

Solution:

Backtracking the problem. Whenever we have the array the size of k we will add that to our set.

Time Complexity :- O(n^k)

'''

class Solution:
    def __init__(self) -> None:
        pass
    def combine(self, n, k):
        
        def recurse(cur,res,idx):
            if len(cur)==k:
                res.add(tuple(cur[:]))
                return
            for i in range(idx,n+1):
                cur.append(i)
                recurse(cur,res,i+1)
                cur.pop()
            return res
        result = set()
        cur = []
        idx=1
        return recurse(cur,result,idx)

if __name__ == "__main__":
    sol = Solution()
    print(sol.combine(4,2))