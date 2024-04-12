'''
Problem 42 (Hard)
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9

2024-04-12-08-34-56.png

'''
class Solution:
    def __init__(self) -> None:
        pass
    def trap(self,height):
        l,r = 0,len(height)-1
        leftmax,rightmax = height[l],height[r]
        res = 0
        while l<r:
            if leftmax<rightmax:
                l+=1
                leftmax = max(height[l],leftmax)
                res+=leftmax-height[l]
            else:
                r-=1
                rightmax = max(height[r],rightmax)
                res+=rightmax+height[r]
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.trap([4,2,0,3,2,5]))
