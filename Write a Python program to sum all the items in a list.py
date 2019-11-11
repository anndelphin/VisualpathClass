#1. Write a Python program to sum all the items in a list.
lst = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)
print("Sum of elements in given list is :", sum(lst))


#2. Write a Python program to multiplies all the items in a list.
#3. Write a Python program to get the largest number from a list.
lis=[]
n=int(input("Enter Items"))
for i in range(n):
    num=int(input("Enter the Nubmer"))
    lis.append(num)
print("The sum of the list elements is:", max(lis))
