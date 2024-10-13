def calculator(a,b,c):
   if c == 1:
       print("sum is ",a + b)
   elif c == 2:
       print("subtract is ",a - b)
   elif c == 3:
       print("multiplication is ",a * b)
   elif c == 4:
       print("division is ",a / b)
   else:
       print("invalid option")
print("calculator")
print("1.add \n 2.subtract \n 3.multiply \n 4.divide")
choise = int(input("enter your choise:"))
num1 = float(input("enter number here:"))
num2 = float(input("enter number here:"))
calculator(num1,num2,choise)