from array import *

# Array in Python

arr=array('i',[])
n=int(input("Enter no. of values : "))

for i in range(n):
  ele=int(input("Enter the values : "))
  arr.append(ele)
  
for i in range(0,n):
  print(arr[i], end =" ")

print("")
# search an element

value=int(input("Enter the value to find : "))
k=0
for i in arr:
  if i==value:
    print(value,"is at index =",k)
    break
  k+=1

  

