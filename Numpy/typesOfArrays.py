from numpy import *

# using array()

arr0=array([1,2,3,4,5])

print(arr0)
print(arr0.dtype)


# array data type

arr1=array([1.2,5.0,3,4.5,6,7])

print(arr1)
print(arr1.dtype)


# using linspace()

arr2=linspace(0,15) #default 50 parts
print(arr2)
arr3=linspace(0,15,20)  #divides 20 parts
print(arr3)


#using arange()

arr4=arange(1,15,2)  # steps 2 numbers
print(arr4)


#using logspace()

arr5=logspace(1,40,5) #
print(arr5[0]) # 1st element
print('%.2f' %arr5[2])  # 3rd element upto 2 decimals


#using zeros()

arr6=zeros(5)
print(arr6)
arr7=zeros(5,int) # want output in integers
print(arr7)

# using ones()

arr8=ones(5)
print(arr8)
arr9=ones(5,int) # want output in integers
print(arr9)
print("")
print("")
# All at once :
print("-----------------------------------------------------")
print("")
print("")
print("1. using array() --> ",arr0)
print("")
print("")
print("2. using float datatype array()  --> ",arr1)
print("")
print("")
print("3. using default linspace() --> ",arr2)
print("")
print("")
print("4. using 20 parts linspace()  -->  ",arr3)
print("")
print("")
print("5. using arange()  --> ",arr4)
print("")
print("")
print("6. using logspace()  --> ",arr5)
print("")
print("")
print("7. using zeros()  --> ",arr6)
print("")
print("")
print("8. using int datatype zeros()  --> ",arr7)
print("")
print("")
print("9. using ones() --> ",arr8)
print("")
print("")
print("10. using int datatype ones()  --> ",arr9)
print("")
print("")
print("-----------------------------------------------------")
