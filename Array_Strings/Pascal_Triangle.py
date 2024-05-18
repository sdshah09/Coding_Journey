'''
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

(Easy)

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 

Constraints:

1 <= numRows <= 30
Seen this question in a real interview before?
1/5
Yes
No
Accepted
1.7M
Submissions
2.2M
Acceptance Rate
74.4%


'''

class Solution:

    def generateRows(self,rows):
        val = 1
        res = [1]
        for col in range(1,rows):
            val = val*(rows-col)
            val = val//(col)
            res.append(val)
        return res

    def generate(self, numRows: int):
        ans = []
        for i in range(1,numRows+1):
            ans.append(self.generateRows(i))
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.generate(5))