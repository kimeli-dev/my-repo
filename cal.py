# creating a simple calculator
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mut(x,y):
    return x*y
def div(x,y):
    if y==0:
        print("syntax error,division with a zero")
    return x/y
print("enter the operation")
print("1. add")
print("2. sub")
print("3. mut")
print("4. div")
choice=input("enter the operation number (1/2/3/4):")
 
if choice in ['1','2','3','4']:
    numb1=float(input("Enter the first operant:"))
    numb2=float(input("enter the operant"))

    if choice=='1':
        print(f"the total is:{add(numb1,numb2)}")
    elif choice=='2':
        print(f"the value is :{sub(numb1,numb2)}")
    elif choice=='3':
        print(f"the results is:{mut(numb1,numb2)}")

    elif choice=='4':
        print(f"the result is:{div(numb1,numb2)}")
else:
 print("ente the correct intergers")
 print("i love coding")
 