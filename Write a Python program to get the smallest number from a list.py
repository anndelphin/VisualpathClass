#3. Write a Python program to get the largest number from a list.
lis=[]
n=int(input("Enter Items"))
for i in range(n):
    num=int(input("Enter the Nubmer"))
    lis.append(num)
print("The sum of the list elements is:", min(lis))


#Write a Python program to multiplies all the items in a list.
NumList=[2,1,4,5,5,5,6,7,7] #The Length of the list consider as starting 1 to n
largest = NumList[0]    
for j in range(1, len(NumList)):
    if(largest > NumList[j]):
        largest = NumList[j]

print("The Smallest Element in this List is : ", largest)


#using sorting Method
k=[1,2,3,4,4,5]
k.sort()
print(k[0])
