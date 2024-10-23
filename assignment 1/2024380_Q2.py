def factorial(n):
    out = 1
    if n == 0:
        return 1
    else:
        for i in range(1,n+1):
            out *= i
        return out

def sin(x):
    out = 0
    x = (3.14/180)*x
    for i in range(0,20):
        out += ((-1)**i)*(x**(2*i+1))/factorial(2*i+1)
    return out

def cos(x):
    x = (3.14/180)*x
    out = 0
    for i in range(0,20):
        out += ((-1)**i)*(x**(2*i))/factorial(2*i)

    return out

def tan(x):
    return sin(x)/cos(x)
    
def height(x,b):
    return tan(x)*b

def distance(x,b):
    return b/cos(x)

def test():
    assert round(sin(30),2) == 0.5
    assert round(cos(60),2) == 0.5
    assert round(tan(45),2) == 1
    assert round(height(45,1),2) == 1
    assert round(distance(45,1),2) == 1.41

test()

a = float(input('enter angle: '))
b = float(input('enter base: '))

print('height:',height(a,b))
print('distance:',distance(a,b))
