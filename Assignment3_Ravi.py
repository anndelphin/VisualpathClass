#8.Write a Python program to check a list is empty or not
k=[1,2,5,4,3]
if len(k)==0:
  print("The List is empty")
else:
  print("Non-Empty list")
  
#9. Write a Python program to clone or copy a list.
k=[1,2,5,4,3]
cp=k.copy()
print("The copied element is:",cp)


#10. Write a Python program to find the list of words that are longer than n from a given list of words.
k=["Ravi","Prasad","karna"]
em=[]
for i in k:
  em.append((len(i),i))
em.sort()
print(em[-1][1])
