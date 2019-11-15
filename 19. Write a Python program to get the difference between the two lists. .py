#19. Write a Python program to get the difference between the two lists. 
k=[1,2,3,4]
l=[1,2,3,4,5]
s=set(k)
x=set(l)
r=s.difference(x)
print(list(r))

#Using sets
print(list(set(k)-set(l)))
