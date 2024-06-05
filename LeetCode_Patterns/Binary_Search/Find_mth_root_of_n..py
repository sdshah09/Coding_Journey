'''
Find the mth root of n

'''

class Solution:
    def findroot(self,m,n):
        l,h = 1,m
        while l<=h:
            mid = (l+h)//2
            res = mid**n
            if(res == m):
                return mid
            elif res>m:
                h = mid-1
            else:
                l = mid+1
        return -1
if __name__ == "__main__":
    sol = Solution()
    print(sol.findroot(625,4))