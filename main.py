try:
    num = int(input("enter number here:"))
    print(num)
except ValueError as ex:
    print("Exception:" ,ex)
print("done")

num = int(input("enter number here:"))
print(num)

try:
    num1 = int(input("enter number here:"))
    num2 = int(input("enter number here:"))
    print(num1/num2)
except ValueError as ex:
    print("Exception:" ,ex)
except ZeroDivisionError as ex:
    print("Exception:" ,ex)
except SyntaxError as ex:
    print("Exception:" ,ex)
finally:
    print("done")