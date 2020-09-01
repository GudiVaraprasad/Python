
print()
print(" Mathematics Simple Calculator ")
print("----------------------------------------------------------------------------")
print("This calculator can perform :  + , - , * , / , // , % , ** ")
print()
print(" NOTE : Enter with only space after each and every character !!!! ")
print()
text = input("Enter : ")

val=text.split()
# print(val)

if val[1]=='+':
    add=int(val[0])+int(val[2])
    print("Addition of ",val[0],"and ",val[2],"= ",add)

elif val[1]=='-':
    sub=int(val[0])-int(val[2])
    print("Subtraction of ",val[0],"and ",val[2],"= ",sub)

elif val[1]=='*':
    mul=int(val[0])*int(val[2])
    print("Multiplication of ",val[0],"and ",val[2],"= ",mul)
    
elif val[1]=='/':
    div=int(val[0])/int(val[2])
    print("division of ",val[0],"and ",val[2],"= ",div)
    
elif val[1]=='//':
    floordiv=int(val[0])//int(val[2])
    print("Quotient from floor division of ",val[0],"and ",val[2],"= ",floordiv)
    
elif val[1]=='%':
    rem=int(val[0])%int(val[2])
    print("Remainder for division of ",val[0],"and ",val[2],"= ",rem)
    
elif val[1]=='**':
    expo=int(val[0])**int(val[2])
    print(val[0],"to the ",val[2],"power = ",expo)

else:
    print("Please Enter again !!")
    print("Note : Enter with only space after each and every character !!!!")

print()    
print("Happy Calculations :) ")
    
