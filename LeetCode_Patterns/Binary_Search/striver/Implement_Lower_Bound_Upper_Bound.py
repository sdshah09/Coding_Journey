'''
Ceil The Floor
Difficulty: EasyAccuracy: 43.76%Submissions: 72K+Points: 2
Given an unsorted array arr[] of integers and an integer x, find the floor and ceiling of x in arr[].

Floor of x is the largest element which is smaller than or equal to x. Floor of x doesn’t exist if x is smaller than smallest element of arr[].
Ceil of x is the smallest element which is greater than or equal to x. Ceil of x doesn’t exist if x is greater than greatest element of arr[].

Return an array of integers denoting the [floor, ceil]. Return -1 as the floor or ceiling value if the floor or ceiling is not present.

Examples:

Input: x = 7 , arr[] = [5, 6, 9, 9, 6, 5, 5, 6]
Output: 6, 8
Explanation: Floor of 7 is 6 and ceil of 7 is 9.
Input: x = 10 , arr[] = [5, 6, 8, 8, 6, 5, 5, 6]
Output: 8, -1
Explanation: Floor of 10 is 8 but ceil of 10 is not possible.
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)


'''

#User function Template for python3

class Solution:
    def getFloorAndCeil(self, x: int, arr: list) -> list:
        # code here
        arr.sort()
        return [self.floor(x,arr),self.ceil(x,arr)]
    def floor(self,x,arr):
        low,high = 0,len(arr)-1
        while low<=high:
            mid = (low+high)//2
            if arr[mid] == x:
                return x
            elif arr[mid]>x:
                high = mid-1
            else:
                low = mid+1
        return arr[high] if high >= 0 else -1
    
    def ceil(self,x,arr):
        low,high = 0,len(arr)-1
        ans = -1
        while low<=high:
            mid = (low+high)//2
            if arr[mid] == x:
                return x
            elif arr[mid]>x:
                ans = arr[mid]
                high = mid-1
            else:
                low = mid+1
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input())
    for _ in range(t):
        x = int(input())
        arr = list(map(int, input().split()))

        ob = Solution()
        ans = ob.getFloorAndCeil(x, arr)
        print(ans[0], ans[1])


if __name__ == "__main__":
    main()

# } Driver Code Ends