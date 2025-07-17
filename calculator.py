def add(x,y):
    print(x+y)

def subtraction(x,y):
    print(x-y)

def division(x,y):
    try:
        print(x/y)
    except ZeroDivisionError:
        print("Cant divide by zero!")

def multi(x,y):
    print(x*y)

x_user=input("Enter first number: ")
y_user=input("Enter second number: ")
x,y=int(x_user),int(y_user)
print("for addition press 1, for sub 2, for div 3, for multi 4")

choice=input("Enter your choice: ")

match choice:
    case "1":
        add(x,y)
    case "2":
        subtraction(x, y)
    case "3":
        division(x, y)
    case "4":
        multi(x, y)

