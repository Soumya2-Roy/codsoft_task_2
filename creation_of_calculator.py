#Design a simple calculator with basic arithmetic operations.
#Prompt the user to input two numbers and an operation choice.
#Perform the calculation and display the result.
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def creation_of_calculator(x,y,sign):
    if sign=='+':
        result=x+y
    elif sign=='-':
        result=x-y
    elif sign=='*':
        result=x*y
    elif sign=='/':
        result=x/y
    else:
        print("Invalid sign")
    print("Result is:",result)
num1=int(input("Enter the value of a:"))
num2=int(input("Enter the value of b:"))
sign=input("Enter the sign of your choice:")
create_calculator(num1,num2,sign)
