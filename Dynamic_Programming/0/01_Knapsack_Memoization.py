'''
Memoization Approach for 0/1 Knapsack Problem:
Note: It should be noted that the above function using recursion computes the same subproblems again and again. See the following recursion tree, K(1, 1) is being evaluated twice. 

In the following recursion tree, K() refers  to knapSack(). The two parameters indicated in the following recursion tree are n and W.
The recursion tree is for following sample inputs.
weight[] = {1, 1, 1}, W = 2, profit[] = {10, 20, 30}

                                                     K(3, 2)  
                                          /                         \ 
                                       /                             \               
                          K(2, 2)                                K(2, 1)
                     /               \                           /               \ 
                  /                   \                       /                   \
          K(1, 2)               K(1, 1)            K(1, 1)       K(1, 0)
           /     \                  /       \                /                  \
        /         \              /           \            /                      \
K(0, 2)  K(0, 1)  K(0, 1)  K(0, 0)  K(0, 1)          K(0, 0)



Recursion tree for Knapsack capacity 2 units and 3 items of 1 unit weight.

As there are repetitions of the same subproblem again and again we can implement the following idea to solve the problem.

If we get a subproblem the first time, we can solve this problem by creating a 2-D array that can store a particular state (n, w). Now if we come across the same state (n, w) again instead of calculating it in exponential complexity we can directly return its result stored in the table in constant time.


'''

# This is the memoization approach of
# 0 / 1 Knapsack in Python in simple
# we can say recursion + memoization = DP


def knapsack(wt, val, W, n):

    # base conditions
    if n == 0 or W == 0:
        return 0
    if t[n][W] != -1:
        return t[n][W]
    # choice diagram code
    if wt[n-1] <= W:
        t[n][W] = max(
            val[n-1] + knapsack(
                wt, val, W-wt[n-1], n-1),
            knapsack(wt, val, W, n-1))
        print(t[n][W])
        print(n,W)
        return t[n][W]
    elif wt[n-1] > W:
        t[n][W] = knapsack(wt, val, W, n-1)
        return t[n][W]

# Driver code
if __name__ == '__main__':
    weight = [1, 1, 1]
    profit = [10, 20, 30]
    W = 2
    n = len(profit)
    
    # We initialize the matrix with -1 at first.
    t = [[-1 for i in range(W + 1)] for j in range(n + 1)]
    print(knapsack(weight, profit, W, n))

# This code is contributed by Prosun Kumar Sarkar
