#12.Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
k=[1,23,3,3,5,3,4]
k=[x for (i,x) in enumerate(k) if i not in (0,4,5)]
print(k)
