'''
1.Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and prints the result.

'''

r = lambda x:x+15
q = lambda x,y:x*y

print(r(10))
print(q(16,3))

'''
2. Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.
Sample Output:

'''

def func(n):
    return lambda x:x*n

result = func(2)
print(result(15))
result = func(4)
print(result(60))


'''
3. Write a Python program to sort a list of tuples using Lambda.
Original list of tuples:
[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
Sorting the List of Tuples:
[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]

'''
scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
scores.sort(key=lambda x: x[1])
print(scores)

'''
4. Write a Python program to sort a list of dictionaries using Lambda.
Original list of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
Sorting the List of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]

'''
phones = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

phones.sort(key = lambda x:x['color'])
print("4: problem, ",phones)

'''
5. Write a Python program to filter a list of integers using Lambda.
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]

'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = list(filter(lambda x:x%2==0,numbers))
odd = list(filter(lambda x:x%2==1,numbers))
print("5: ",even)
print("6: ",odd)

'''
6. Write a Python program to square and cube every number in a given list of integers using Lambda.
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Square every number of the said list:
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Cube every number of the said list:
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

'''
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# square(nums)

square = list(map(lambda x:x**2,nums))
cube = list(map(lambda x:x**3,nums))
print("Problem 6: ",square,cube)

'''
7. Write a Python program to find if a given string starts with a given character using Lambda.
Sample Output:
True
False

'''
starts_with = lambda s:True if s.startswith('P') else False
print(starts_with("rint"))

'''
8. Write a Python program to extract year, month, date and time using Lambda.
Sample Output:
2020-01-15 09:03:32.744178
2020
1
15
09:03:32.744178

'''
import datetime
now = datetime.datetime.now()
print(now)
year,month,day = lambda x:x.year,lambda x:x.month, lambda x:x.day
print(year(now),month(now),day(now))
time = lambda x:x.time()
print(time(now))

'''
9. Write a Python program to check whether a given string is a number or not using Lambda.
Sample Output:
True
True
False
True
False
True
Print checking numbers:
True
True

Check decimal as well as numbers but will return False with negative number 
'''
isNumber = lambda x:x.replace('.','',1).isdigit()
print(isNumber('-123'))

'''
10. Write a Python program to create Fibonacci series up to n using Lambda.
Fibonacci series upto 2:
[0, 1]
Fibonacci series upto 5:
[0, 1, 1, 2, 3]
Fibonacci series upto 6:
[0, 1, 1, 2, 3, 5]
Fibonacci series upto 9:
[0, 1, 1, 2, 3, 5, 8, 13, 21]

'''

from functools import reduce 
fibonacci = lambda n:reduce(lambda x,_:x+[x[-1]+x[-2]],range(n-2),[0,1])
print(fibonacci(5))

'''
11. Write a Python program to find the intersection of two given arrays using Lambda.
Original arrays:
[1, 2, 3, 5, 7, 8, 9, 10]
[1, 2, 4, 8, 9]
Intersection of the said arrays: [1, 2, 8, 9]

'''

n = [1, 2, 3, 5, 7, 8, 9, 10]
m =[1, 2, 4, 8, 9]
intersection = lambda x,y:list(a for a in y if a in x)
print(intersection(n,m))

'''
12. Write a Python program to rearrange positive and negative numbers in a given array using Lambda.
Original arrays:
[-1, 2, -3, 5, 7, 8, 9, -10]
Rearrange positive and negative numbers of the said array:
[2, 5, 7, 8, 9, -10, -3, -1]

'''
nums = [-1, 2, -3, 5, 7, 8, 9, -10]
positive = list(filter(lambda x:x>0,nums))
negative = list(filter(lambda x:x<0,nums))
print(positive+negative)

result = sorted(nums, key=lambda i: 0 if i == 0 else -1 / i)

'''
Let’s go through each part of this key function.

0 if i == 0:

If i is zero, the lambda returns 0. This means that zeros will have a sorting key of 0.
This ensures that all zeros are grouped together since they have the same sorting key.
else -1 / i:

For non-zero values, the lambda returns -1 / i. This produces a sorting key that is based on the reciprocal of i but with a negative sign.
This negative reciprocal affects the order:
For positive numbers: -1 / i is negative, so larger positive numbers (smaller -1 / i values) come before smaller positive numbers (larger -1 / i values).
For negative numbers: -1 / i is positive, so smaller negative numbers (smaller -1 / i values) come before larger negative numbers (larger -1 / i values).

'''

'''
13. Write a Python program to count the even and odd numbers in a given array of integers using Lambda.
Original arrays:
[1, 2, 3, 5, 7, 8, 9, 10]
Number of even numbers in the above array: 3
Number of odd numbers in the above array: 5

'''
nums = [1, 2, 3, 5, 7, 8, 9, 10]
odd = len(list(filter(lambda x:x%2==1,nums)))
even = len(list(filter(lambda x:x%2==0,nums)))
print(odd,even)

'''
14. Write a Python program to filter a given list to determine if the values in the list have a length of 6 using Lambda.
Sample Output:
Monday
Friday
Sunday

'''
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

length_list = list(filter(lambda x:len(x)==6, weekdays))
print(length_list)

'''
15. Write a Python program to add two given lists using map and lambda.
Original list:
[4, 5, 6]
Result: after adding two list
[5, 7, 9]

'''
m = [1, 2, 3]
n = [4, 5, 6]
add_list = list(map(lambda x,y:x+y,m,n))
print(add_list)

'''
16. Write a Python program to find the second lowest total marks of any student(s) from the given names and marks of each student using lists and lambda. Input the number of students, the names and grades of each student.
Input number of students: 5
Name: S ROY
Grade: 1
Name: B BOSE
Grade: 3
Name: N KAR
Grade: 2
Name: C DUTTA
Grade: 1
Name: G GHOSH
Grade: 1
Names and Grades of all students:
[['S ROY', 1.0], ['B BOSE', 3.0], ['N KAR', 2.0], ['C DUTTA', 1.0], ['G GHOSH', 1.0]]
Second lowest grade: 2.0
Names:
N KAR

'''

# # Input number of students
# num_students = int(input("Input number of students: "))

# # Collect names and grades for each student
# students = []
# for _ in range(num_students):
#     name = input("Name: ")
#     grade = float(input("Grade: "))
#     students.append([name, grade])

# # Display all student names and grades
# print("Names and Grades of all students:")
# print(students)

# # Find the second-lowest grade
# # 1. Extract unique grades and sort them
# unique_grades = sorted(set([student[1] for student in students]))

# # 2. Get the second lowest grade
# if len(unique_grades) > 1:
#     second_lowest_grade = unique_grades[1]
# else:
#     print("Not enough unique grades to determine the second lowest.")
#     exit()

# print(f"Second lowest grade: {second_lowest_grade}")

# # Find students with the second lowest grade using a lambda filter
# second_lowest_students = list(filter(lambda x: x[1] == second_lowest_grade, students))

# # Extract names of students with the second lowest grade
# names_with_second_lowest = sorted([student[0] for student in second_lowest_students])

# print("Names:")
# for name in names_with_second_lowest:
#     print(name)

'''
Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda.


'''
nums = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
result = list(filter(lambda x: (x % 19 == 0 or x % 13 == 0), nums))
print(result)

'''
18. Write a Python program to find palindromes in a given list of strings using Lambda.

'''
y = ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
res = list(filter(lambda x:x==x[::-1],y))
print(res)

'''
19. Write a Python program to find all anagrams of a string in a given list of strings using Lambda.
Orginal list of strings:
['bcda', 'abce', 'cbda', 'cbea', 'adcb']
Anagrams of 'abcd' in the above string:
['bcda', 'cbda', 'adcb']

'''
from collections import Counter
str = "abcd"
texts = ['bcda', 'abce', 'cbda', 'cbea', 'adcb']
result = list(filter(lambda x: (Counter(str) == Counter(x)), texts))
print(result)

'''
20. Write a Python program to find the numbers in a given string and store them in a list. Afterward, display the numbers that are longer than the length of the list in sorted form. Use the lambda function to solve the problem.
Original string: sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5
Numbers in sorted form:
20 23 56

'''
s = "sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5"
z = list(filter(lambda x:x if x.isdigit() else '',s.split()))
y = list(filter(lambda x:int(x) if int(x)>len(z) else '',z))
result = sorted(list(filter(lambda x: int(x) > len(s.split()), filter(lambda x: x.isdigit(), s.split()))))

print(sorted(y))
# res = list(filter(lambda x:x>len(s),s.split()))

'''
21. Write a Python program that multiplies each number in a list with a given number using lambda functions. Print the results.
Original list: [2, 4, 6, 9, 11]
Given number: 2
Result:
4 8 12 18 22


'''
nums = [2, 4, 6, 9, 11]
n = 2
res = list(map(lambda x:x*n,nums))
print(res)

'''
22. Write a Python program that sums the length of a list of names after removing those that start with lowercase letters. Use the lambda function.
Result:
16

'''
sample_names = ['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']
# Filter the 'sample_names' list using a lambda function to include only names that start with an uppercase letter
# followed by lowercase letters for the rest of the name
sample_names = list(filter(lambda el: el[0].isupper() and el[1:].islower(), sample_names))
summ = sum(len(name) for name in s)
print(summ)

'''
23. Write a Python program to calculate the sum of the positive and negative numbers of a given list of numbers using the lambda function.
Original list: [2, 4, -6, -9, 11, -12, 14, -5, 17]
Sum of the positive numbers: -32
Sum of the negative numbers: 48

'''
nums = [2, 4, -6, -9, 11, -12, 14, -5, 17]
pos = sum(list(filter(lambda x:x>0,nums)))
neg = sum(list(filter(lambda x:x<0, nums)))
print(pos,neg)

'''
24. Write a Python program to find numbers within a given range where every number is divisible by every digit it contains.
Sample Output:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

'''
def divisible_by_digits(start_num, end_num):
    # Return a list comprehension that generates a list of numbers within the range of start_num to end_num (inclusive)
    # The list comprehension filters numbers based on a condition specified in the 'if' statement
    return [
        n for n in range(start_num, end_num + 1)
        if not any(map(lambda x: int(x) == 0 or n % int(x) != 0, str(n)))
    ]

# Print the result of calling the 'divisible_by_digits' function with arguments 1 and 22
# print(divisible_by_digits(1, 22))

'''
26. Write a Python program to find a list with maximum and minimum length using lambda.
Original list:
[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
List with maximum length of lists:
(3, [13, 15, 17])
List with minimum length of lists:
(1, [0])

'''
# Define a function 'max_length_list' that takes a list of lists 'input_list' as input
def max_length_list(input_list):
    # Calculate the maximum length of the sublists in 'input_list'
    max_length = max(len(x) for x in input_list)
    
    # Find the sublist with the maximum length using the 'max' function and a lambda function
    max_list = max(input_list, key=lambda i: len(i))
    
    # Return a tuple containing the maximum length and the sublist with the maximum length
    return (max_length, max_list)

# Define a function 'min_length_list' that takes a list of lists 'input_list' as input
def min_length_list(input_list):
    # Calculate the minimum length of the sublists in 'input_list'
    min_length = min(len(x) for x in input_list)
    
    # Find the sublist with the minimum length using the 'min' function and a lambda function
    min_list = min(input_list, key=lambda i: len(i))
    
    # Return a tuple containing the minimum length and the sublist with the minimum length
    return (min_length, min_list)

# Create a list of lists named 'list1'
list1 = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]

# Print the original list 'list1'
print("Original list:")
print(list1)

# Print the list with the maximum length of sublists within 'list1'
print("\nList with maximum length of lists:")
print(max_length_list(list1))

# Print the list with the minimum length of sublists within 'list1'
print("\nList with minimum length of lists:")
print(min_length_list(list1))

'''
27. Write a Python program to sort each sublist of strings in a given list of lists using lambda.
Original list:
[['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]
After sorting each sublist of the said list of lists:
[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]

'''
color1 = [["green", "orange"], ["black", "white"], ["white", "black", "orange"]]

res = [sorted(x,key = lambda x:x[0]) for x in color1] # x[0] meaning it will sort according to every first character of the string 
print(res)

'''
28. Write a Python program to sort a given list of lists by length and value using lambda.
Original list:
[[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
Sort the list of lists by length and value:
[[0], [2], [0, 7], [1, 3], [9, 11], [13, 15, 17]]

'''
nums = [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
res = [sorted(nums,key = lambda x:(len(x),x))]
print(res)
