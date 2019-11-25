'''def last(n): 
    return n[-1]

def sort_list_last(tuples):
  return sorted(tuples, key=last)

print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))
'''

a=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print(len(a))
for j in range (1,len(a)) :
  for i in range(len(a)-j) :
    if a[i][1]>a[i+1][1] :
      temp=a[i]
      a[i]=a[i+1]
      a[i+1]=temp
for i in range(len(a)) :
  print(a[i])
