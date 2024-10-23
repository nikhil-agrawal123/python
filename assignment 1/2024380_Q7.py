import math
z = int(input('enter a number to find from'))

def gcd(a,b):
    if (a == 0 and b == 1) or (b==0 and a==1):
        return 1
    elif a>0 :
        while b:
            a , b = b, a % b
        return a

def visible(x):
    out = 0
    for i in range(x+1):
        for j in range(x+1):
            if gcd(i,j) == 1:
                out +=1
    return out

def density(y):
    return visible(y)/(y*y)

def converge(x):
    i = 1
    while True:
        if abs(density(i) - (6/math.pi**2))/(6/math.pi**2) <= (x/100):
            return i
        i += 1

print(converge(float(input('Enter a percentage to find from '))))