def polynomail(x):
    return x**3 - 10.5*x**2 + 34.5*x - 35

def slope(x):
    return 3*x**2 - 21*x + 34.5

def roots(x): 
    while x<100:
        x1 = x - polynomail(x)/slope(x)
        if abs(x1-x) <= 0.2:
            return x1
        else:
            if x1 != x:
                x = x1
            else:
                return "No such root exists"

def test():
    assert polynomail(0) == -35
    assert slope(0) == 34.5
    assert roots(0) == 1.992402021259231

test()

x = float(input('Enter a starting point: '))
print(roots(x))



#bonus

def multi_roots(x,y):
    b = []
    for i in range(x,y+1):
        y = roots(i)
        if polynomail(y) == 0 or polynomail(y) <= 0.000001: #the first condition gives integer roots for approximation of decimal roots used the second equation
            if y not in b:
                b.append(y)
    return b
#print(multi_roots(float(input('Enter a starting point: ')),float(input('Enter a ending point: '))))

