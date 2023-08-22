# This function adds two numbers
def add(x,y):
    return x + y
# This function subracts two numbers
def subtract(x,y):
     return x - y
# This function multiplies two numbers
def multiply(x,y):
    return x * y
# This function divides two nubers
def divide(x,y):
    return x / y


print("select operation.")
print("1.Add")
print("2,Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    #take input from the user
    choice=input("nter choice(1/2/3/4): ")
    
    # check if choice is one of the four options
    if choice in ('1','2','3','4'):
        try:
            num1 = float(input("Enter first number:"))
            num -= float(input("Enter second number:"))
        except ValueError:
            print("Invalid input.Please enter anumber.")
            continue
        
        if choice =='1':
            print(num1, "+", num2, "=", add(num1, num2))
            
        elif choice =='2':
            print(num1, "")