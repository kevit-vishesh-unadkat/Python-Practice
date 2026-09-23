# try except block program

a=int(input("enter a number  :"))
b=0

try:
    print(a/b)
except ZeroDivisionError:
    print("You can not any number divide by zero")
except Exception as e:
    print(e)


