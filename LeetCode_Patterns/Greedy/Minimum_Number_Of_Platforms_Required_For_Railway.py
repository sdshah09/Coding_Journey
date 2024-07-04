'''
Problem Statement: We are given two arrays that represent the arrival and departure times of trains that stop at the platform. We need to find the minimum number of platforms needed at the railway station so that no train has to wait.

Examples 1:

Input: N=6, 
arr[] = {9:00, 9:45, 9:55, 11:00, 15:00, 18:00} 
dep[] = {9:20, 12:00, 11:30, 11:50, 19:00, 20:00}

Output:3
Explanation: There are at-most three trains at a time. The train at 11:00 arrived but the trains which had arrived at 9:45 and 9:55 have still not departed. So, we need at least three platforms here.


Example 2:

Input Format: N=2, 
arr[]={10:20,12:00}
dep[]={10:50,12:30}

Output: 1
Explanation: Before the arrival of the new train, the earlier train already departed. So, we don't require multiple platforms.

Solution
'''

class Solution:
    def countPlatforms(self,n, arr, dep):
        arr.sort()
        dep.sort()        
        ans = 1
        count = 1
        i = 1
        j = 0
        while i<len(arr) and j<len(dep):
            if arr[i]<=dep[j]:
                count+=1 # one more platform needed
                i+=1 # going on next arrival point
            else:
                count-=1 # no need of extra platform
                            # meaning the train has departure
                j+=1
            ans = max(ans,count)
        return ans
if __name__ == "__main__":
    arr = [900, 940, 950, 1100, 1500, 1800]
    dep = [910, 1200, 1120, 1130, 1900, 2000]
    # arr = [1020,1200]
    # dep = [1050,1230]
    n = len(dep)
    sol = Solution()
    print("Minimum number of Platforms required", sol.countPlatforms(n, arr, dep))
