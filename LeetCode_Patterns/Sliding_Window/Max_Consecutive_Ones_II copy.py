'''
487. Max Consecutive Ones II (Medium) (Premium)
Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.

Example 1:
Input: [1,0,1,1,0]
Output: 4
Explanation: Flip the first zero will get the the maximum number of consecutive 1s.
    After flipping, the maximum number of consecutive 1s is 4.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
Follow up:
What if the input numbers come in one by one as an infinite stream? In other words, you can't store all numbers coming from the stream as it's too large to hold in memory. Could you solve it efficiently?

Using Sliding window technique to check for every condition. The question you can flip at most one 0 so we have to check untile we can find two zeros consecuitvely.
'''

class Solution:
    def __init__(self) -> None:
        pass
    def sliding_window(self,nums):
        left,right = 0,0
        count_of_zeros = 0
        global_max = 0

        while right<len(nums):
            if nums[right]==0:
                count_of_zeros+=1
            while count_of_zeros==2:
                global_max = max(global_max,right-left)
                if nums[left]==0:
                    count_of_zeros-=1
                left+=1
            right+=1
        if count_of_zeros<2:
            global_max = max(global_max,right-left)
        return global_max

if __name__ == "__main__":
    sol = Solution()
    print(sol.sliding_window([1,0,0,1,1,1,1,1]))