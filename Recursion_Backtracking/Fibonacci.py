'''
Create a Fibonacci sequence until the given range
Time Complexity:- O(2^n)
'''

class Solution:
    def __init_(self):
        pass
    def fibonacci(self,n):
        if n<=1:
            return n
        return self.fibonacci(n-1)+self.fibonacci(n-2)
if __name__ == "__main__":
    sol = Solution()
    n = [sol.fibonacci(i) for i in range(9)]
    print(n)