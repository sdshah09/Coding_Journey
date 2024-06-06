import heapq

class Solution:
    def maxHeap(self,nums,k):
        arr = []
        heapq.heapify(arr)
        for i in nums:
            heapq.heappush(arr,-i)
            if len(arr)>k:
                heapq.heappop(arr)
        return -arr[0]
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxHeap([1, 23, 12, 13, 30, 2, 50], 3))