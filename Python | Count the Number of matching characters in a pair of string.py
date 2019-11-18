#Python | Count the Number of matching characters in a pair of string
str1="RaviP"
str2="Ra"
c=0
j=0
for i in str1:
    if str2.find(i)>=0 and j==str1.find(i):
        c+=1
    j+=1
print("Number of character maching is ",c)


#Python | Count the Number of matching characters in a pair of string
str1="RaviP"
str2="Ra"
s1=set(str1)
s2=set(str2)
m=s1&s2
print("the Number of matched Elements in the strings are:",str(len(m)))



st="Ravi12"
s="Rav"
c=0
j=0
for i in st:
    if i in s:
        c+=1
    
print(c)
