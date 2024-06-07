'''
Given an array of N elements, where each element is at most K away from its target position, devise an algorithm that sorts in O(N log K) time.

Examples: 

Input: arr[] = {6, 5, 3, 2, 8, 10, 9}, K = 3 
Output: arr[] = {2, 3, 5, 6, 8, 9, 10}

Input: arr[] = {10, 9, 8, 7, 4, 70, 60, 50}, k = 4
Output: arr[] = {4, 7, 8, 9, 10, 50, 60, 70}


This is a heap problem. What we will do is we will add the elements in minHeap until j and then pop that element and add that element for array sorting until k times.

'''

import heapq

def sort_heap(arr, k):
    if not arr or k < 0:
        return  # Handle edge cases where the input is invalid

    heap = []
    n = len(arr)
    i = 0

    # Add the first k+1 elements to the heap
    for i in range(min(k + 1, n)):
        heapq.heappush(heap, arr[i])

    index = 0

    for i in range(k + 1, n):
        arr[index] = heapq.heappop(heap)
        heapq.heappush(heap, arr[i])
        index += 1

    # Extract remaining elements from the heap
    while heap:
        arr[index] = heapq.heappop(heap)
        index += 1

# Example usage
arr = [1, 4, 5, 2, 3, 8, 7, 6]
k = 2
sort_heap(arr, k)
print(arr)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]
