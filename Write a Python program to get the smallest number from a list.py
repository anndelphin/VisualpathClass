#3.Write a Python program to get the largest number from a list.
#4.Write a Python program to get the smallest number from a list.
ls = [1, 2, 3, 0, 9, 7]
ls.sort()
print(ls)
print("The Largest element in the list",ls[-1])
print("The smallest element in the list",ls[0])
#Using in builtin Functions
print("The Largest element in the list",max(ls))
print("The smallest element in the list",min(ls))
