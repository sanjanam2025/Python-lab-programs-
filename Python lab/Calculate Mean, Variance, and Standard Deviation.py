from math import sqrt
mylist =[]
tot=0
n=int(input('Enter the number of items:'))
print('Enter',n,'the items:')
for i in range(n):
    item =int(input())
    mylist.append(item)
    tot+=item
mean= tot/n
tot=0
for item in mylist:
    tot+=(item-mean)*(item-mean)
var=tot/n
std=sqrt(var)
print("mean=",mean)
print("variance=",var)
print("standard deviation=",std)