'''
Connect n ropes with minimum cost
Last Updated : 19 May, 2023
Given are N ropes of different lengths, the task is to connect these ropes into one rope with minimum cost, such that the cost to connect two ropes is equal to the sum of their lengths.

Examples:

Input: arr[] = {4,3,2,6} , N = 4
Output: 29
Explanation: 

First, connect ropes of lengths 2 and 3. Now we have three ropes of lengths 4, 6, and 5. 
Now connect ropes of lengths 4 and 5. Now we have two ropes of lengths 6 and 9. 
Finally connect the two ropes and all ropes have connected.

'''
import heapq
 
 
def minCost(arr, n): 
    heapq.heapify(arr)
    res = 0
    while(len(arr) > 1):
        first = heapq.heappop(arr)
        second = heapq.heappop(arr)
        res += first + second
        heapq.heappush(arr, first + second)
 
    return res
 
if __name__ == '__main__':
 
    lengths = [4, 3, 2, 6]
    size = len(lengths)
 
    print("Total cost for connecting ropes is " +
          str(minCost(lengths, size)))
