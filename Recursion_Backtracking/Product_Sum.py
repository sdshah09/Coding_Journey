'''
Write a function that takes in a "special" array and returns its product sum.

A "special" array is a non-empty array that contains either integers or other "special" arrays. The product sum of a "special" array is the sum of its elements, where "special" arrays inside it are summed themselves and then multiplied by their level of depth.

The depth of a "special" array is how far nested it is. For instance, the depth of [] is 1; the depth of the inner array in [[]] is 2; the depth of the innermost array in [[[]]] is 3.

Therefore, the product sum of [x, y] is x + y; the product sum of [x, [y, z]] is x + 2 * (y + z); the product sum of [x, [y, [z]]] is x + 2 * (y + 3 * z).

Sample Input

array = [5, 2, [7, -1], 3, [6, [-13, 8]], 4]
'''

# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array,count=1):
    # Write your code here.
    val = 0
    for i in array:
        if type(i) is list:
            val+=productSum(i,count+1)
        else:
            val+=i
    print(val)
    return val*count
x = productSum([5, 2, [7, -1], 3, [6, [-13, 8], 4]])
print(x)