#Write a Python program that takes three numbers from the user and prints the largest number.
num1= int(input("enter the number :",))
num2= int(input("enter the number :",))
num3= int(input("enter the number:",))
# now comparing the three numbers 
if num1>= num2 and num1>=num3:
    print("largest number is num1", num1)
elif num2>=num1 and num2>=num3:
    print("largest number is num2", num2)
else :
    print("largest number is num3", num3)
