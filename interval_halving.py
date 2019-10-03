def func(x):
    if(x!=0):
        f = float((x*x)+(54/x))
    else:
        f = float(100000.00)
    return f

def main():
    print("\n *** INTERVAL HALVING METHOD *** \n")
    a = int(input("Enter the lower bound : "))
    b = int(input("Enter the upper bound : "))
    n = float(input("Enter the small number : "))
    
    f = 0
    
    while(True):
        xm = (a+b)/2
        len = int(abs(b-a))
        x1 = a + (len/4)
        x2 = b - (len/4)
        
        if(func(x1)<func(xm)):
            b = xm
            xm = x1
        elif(func(x2)<func(xm)):
            a = xm
            xm = x2
        else:
            a = x1
            b = x2
            
        if(float(len)<n):
            f = 1
            break
        else:
            f = 0
            continue


    if(f==1):
        print("Minimum lies between {} and {} ".format(a,b))
        print("Minimum value is {}".format(xm))
    else:
        print("Minimum not found")

if(__name__=='__main__'):
    main()
