'''
Three way partitioning of an array around a given range
Last Updated : 20 Feb, 2023
Given an array and a range [lowVal, highVal], partition the array around the range such that array is divided in three parts. 

All elements smaller than lowVal come first. 
All elements in range lowVal to highVal come next. 
All elements greater than highVal appear in the end. 
The individual elements of the three sets can appear in any order.

A two partition Quick Sort would pick a value, say 4, and put every element greater than 4 on one side of the array and every element less than 4 on the other side. Like so:

3, 2, 0, 2, 4, | 8, 7, 8, 9, 6, 5
A three partition Quick Sort would pick two values to partition on and split the array up that way. Lets choose 4 and 7:

3, 2, 0, 2, | 4, 6, 5, 7, | 8, 8, 9
It is just a slight variation on the regular quick sort.

Input: arr[] = {1, 14, 5, 20, 4, 2, 54, 20, 87, 98, 3, 1, 32}  , lowVal = 14 , highVal = 20
Output: arr[] = {1, 5, 4, 2, 1, 3, 14, 20, 20, 98, 87, 32, 54}
Explanation: all elements which are less than 14 are present in the range of 0 to 6
                       all elements which are greater than 14 and less than 20 are present in the range of 7 to 8
                       all elements which are greater than 20 are present in the range of 9 to 12        

Input: arr[] = {1, 14, 5, 20, 4, 2, 54, 20, 87, 98, 3, 1, 32} , lowVal = 20 , highVal = 20     
Output: arr[] = {1, 14, 5, 4, 2, 1, 3, 20, 20, 98, 87, 32, 54} 



'''
class Solution:
    # def threeway(self, nums, lowVal, highVal):
    #     l, m, r = 0, 0, len(nums) - 1
        
    #     while m <= r:
    #         if nums[m] < lowVal:
    #             nums[m], nums[l] = nums[l], nums[m]
    #             l += 1
    #             m += 1
    #         elif nums[m] > highVal:
    #             nums[m], nums[r] = nums[r], nums[m]
    #             r -= 1
    #         else:
    #             m += 1
                
    #     return nums
    from itertools import chain

    def sort_list_ranges(self,input_list, low, high):

        sorted_list = [[] for _ in range(3)]

        for elem in input_list:
            if elem < low:
                sorted_list[0].append(elem)
            elif elem > high:
                sorted_list[2].append(elem)
            else:
                sorted_list[1].append(elem)

        return [item for sublist in sorted_list for item in sublist]



if __name__ == "__main__":
    sol = Solution()
    result = sol.sort_list_ranges([1, 14, 5, 20, 4, 2, 54, 20, 87, 98, 3, 1, 32], 1, 5)
    print(result)
