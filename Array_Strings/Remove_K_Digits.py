'''
Problem 402 (Medium)
Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

 

Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.

Solution:- 
        We will remove the element from a stack if the element is stack is greater than current
        element. This will ensure that the minimum number of values stay in the stack and we
        will return that stack


'''

class Solution:
    def __init__(self) -> None:
        pass
    def removedigits(self,num,k):
        res = []
        stack=[]
        for i in range(len(num)):
            while k>0 and stack and stack[-1]>num[i]:
                stack.pop()
                k-=1
            stack.append(num[i])
        stack=stack[:len(stack)-k]
        result="".join(stack).lstrip("0") 
        return result if result else "0"
if __name__ == "__main__":
    sol = Solution()
    print(sol.removedigits("14432",2))