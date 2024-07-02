'''
Given N items where each item has some weight and profit associated with it and also given a bag with capacity W, [i.e., the bag can hold at most W weight in it]. The task is to put the items into the bag such that the sum of profits associated with them is the maximum possible. 

Note: The constraint here is we can either put an item completely into the bag or cannot put it at all [It is not possible to put a part of an item into the bag].

Input: N = 3, W = 4, profit[] = {1, 2, 3}, weight[] = {4, 5, 1}
Output: 3
Explanation: There are two items which have weight less than or equal to 4. If we select the item with weight 4, the possible profit is 1. And if we select the item with weight 1, the possible profit is 3. So the maximum possible profit is 3. Note that we cannot put both the items with weight 4 and 1 together as the capacity of the bag is 4.

Input: N = 3, W = 3, profit[] = {1, 2, 3}, weight[] = {4, 5, 6}
Output: 0

Follow the below steps to solve the problem:

The maximum value obtained from ‘N’ items is the max of the following two values. 

Case 1 (include the Nth item): Value of the Nth item plus maximum value obtained by remaining N-1 items and remaining weight i.e. (W-weight of the Nth item).
Case 2 (exclude the Nth item): Maximum value obtained by N-1 items and W weight.
If the weight of the ‘Nth‘ item is greater than ‘W’, then the Nth item cannot be included and Case 2 is the only possibility.

'''

class Solution:
    # This is a Recursive Solution
    def knapSack(self,W, wt, val, n):
        if n==0 or W ==0:
            return 0 # Base case that whenver the solution reach it's peak
        # There are 3 choices where we can find the maximum profit.
        # If the current weight is more than the given weight we do not consider that option
        # If the current weight is less than the given weight then there will be 2 choices.Either we take consider the weight for maximum profit or we do not.
        
        if wt[n-1]<=W:
            return max(val[n-1]+self.knapSack(W-wt[n-1],wt,val,n-1),self.knapSack(W,wt,val,n-1))
        else:
            return self.knapSack(W,wt,val,n-1)
    
if __name__ == '__main__':
    sol = Solution()
    profit = [60, 100, 120]
    weight = [10, 20, 30]
    W = 50
    n = len(profit)
    print(sol.knapSack(W, weight, profit, n))
