#7. Write a Python program to remove duplicates from a list. 
k=[2,2,2,2,4,5,6,1]
z=list(set(k))
print(z)

#Using Function
def z(k):
  f=[]
  for i in k:
    if i not in f:
      f.append(i)
  return f
  
k=[2,2,2,2,4,5,6,1]
#z=list(set(k))
print(z(k))

#Using Normal Loop
k=
