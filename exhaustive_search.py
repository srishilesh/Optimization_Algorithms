print("\n *** EXHAUSTIVE SEARCH METHOD *** \n")
a = int(input("Enter the lower bound : "))
b = int(input("Enter the upper bound : "))
n = int(input("Enter the number of steps : "))

def func(x):
    if(x!=0):
        f = (x*x) + (54/x)
    else:
        f = 100000
    return f

cx = (b-a)/n

x1 = a
x2 = x1 + cx
x3 = x2 + cx
f = 0
while(True):
    if(func(x1)>=func(x2) and func(x2)<=func(x3)):
        f = 1
        break
    else:
        f = 0
        x1 = x2
        x2 = x3
        x3 = x2 + cx

if(f==1):
    print("Minimum lies between {} and {} ".format(x1,x3))
else:
    print("Minimum not found")

