'''def add(x,y):
    z=x+y
    return z
x=add(10,20)
print(x)
p=int(input("enter any no:"))  
q=int(input("enter any no:")) 
r=add(p,q)
print(r)'''
'''def add(x,y):
    z=(x+y)
    print(z)
p=int(input("enter any no:"))  
q=int(input("enter any no:")) 
#add(p,q)
print(add(p,q))'''
'''def add(x=0,y=0):
    z=x+y
    return z
p=int(input("enter any no:"))  
x=add(p)
print(x)'''
#============variable-length argument(argu)========>
'''def add(*x):
    add=0
    for i in x:
        add=add+i
    print("add=",add)
add(10,20)
add(10,20,30,40)'''
#===========keyword variable length argument(**kwargs)
'''def employee_data(**data):
    for i,j in data.items():
        #print(i,"=",j)
        print(j)
employee_data(name="sanchita",city="bhopal")'''
#<===================variavle scope===================>
#local
#global
#<====local scope variable===>
'''def add(x):
    y=10
    sum=x+y
    print(sum)
add(10)'''
#<====global scope variable===>
'''y=10
def add(x):
    sum=x+y
    print(sum)
add(10)
print(y)'''
#<====local ,global both scope variable===>
'''y=10
def add(x):
    y=10
    sum=x+y
    print(sum)
add(10)
print(y)'''
#=========global priority fisrt ====>
#global in built method h
'''y=10
def add(x):
    sum=x+globals()['y']
    print(sum)
add(10)
print(y)'''
#global 
'''def add(x):
    global y
    y=10
    sum=x+y
    print(sum)
add(10)
print(y)'''
'''y=20
def add(x):
    global y
    y=10
    sum=x+y
    print(sum)

add(y)
print(y)
y=30
print(y)'''
#<=====================calculator using function=================>
'''def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2

while True:
    print("Please select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n"
        "5. Break\n")
    n = int(input("Select operations form 1, 2, 3, 4, 5 :"))
    
    number_1 = int(input("Enter first number: "))
    number_2 = int(input("Enter second number: "))
    
    if n== 1:
        print(number_1, "+", number_2, "=",
                        add(number_1, number_2))
    
    elif n == 2:
        print(number_1, "-", number_2, "=",
                        sub(number_1, number_2))
    
    elif n == 3:
        print(number_1, "*", number_2, "=",
                        multiply(number_1, number_2))
    
    elif n == 4:
        print(number_1, "/", number_2, "=",
                        divide(number_1, number_2))
    elif n == 5:
        break
    else:
        print("Invalid input")'''
'''my_list=[10,20,30,40,50]
new_list=[]
for i in my_list:
    x=i+5
new_list.append[x]
print(new_list)'''
#================map=================>

'''my_list=[10,20,30,40,50]
def add(x):
    return x+5
x=map(add,my_list)
print(x)
print(list(x))'''
'''n=int(input("enter any name:"))


n(ord('n'))'''
'''x=input("enter any name:")
def add(x):
    x=ord(x)
    y=x+5
    return chr(x)

y=map(add,x)
#<======filter=================>
print(f"ASCII value of '{chr}' is: {y}")'''
'''my_list=[10,15,20,25,30,35]
def greater(x):
    if x>=20:
        return True
x=filter(greater,my_list)
print(my_list)'''
#yield is a key word it is use for generator instance 
#new function