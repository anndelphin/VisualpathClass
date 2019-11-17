#Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings

k=["RaviR",'12121']
c=0
for i in k:
    if len(i) > 1 and i[0]==i[-1]:
        c+=1
print(c)
