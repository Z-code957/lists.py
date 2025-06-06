"""Lists
Outline:
Write a program to perform the following operations on a List: 1. Create an empty list 2.
 A list with elements 3. Use * operator 4. Reverse a list"""

number = []
#print(number)
#items = [1,2,3,"book","pen",True]
#print(items)
#multiply = [5,6,7]*3
"""a = [10,20,30,40,50]
b = a[::-1]
print(b)"""

"""Word Matching
Outline:
Write a Python program to count the number of strings where the string length is two or more,
 and the first and last characters are the same from a given list of strings."""
"""def match(words):
    character = 0
    lst = []
    for i in words:
        if len(i)>1 and i[0]==i[-1]:
            character+=1
            lst.append(i)
    print("List of the words with 1st and last character same ",lst)
    return character
count = match(["sahas","tent","adity","book","laptop"])
print("Number of words having 1st and last character as same ",count)"""

"""Play with Lists
Outline:
Write a Python program to find the sum and average of the list.
 The average of the list is defined as the sum of the elements divided by the number of the elements. Also, find the largest and the smallest number in the list."""
l= [4, 5, 1, 2, 9, 7, 10, 8]
count = 0
for i in l:
    count += i
print("Sum of all the values is ",count)
average = count/len(l)
print("Average = ",average)
print(l.sort())
print(l[0])
print(l[-1])