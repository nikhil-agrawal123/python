def dydx(x,y):
    return x+y

def output(x,y):
    y_init = 1

    while x<y:
        y_new = y_init + 0.1*dydx(x,y_init)
        x = x+0.1
        y_init = y_new

    return (y_new)

def test():
    assert dydx(0,1) == 1
    assert output(0,1) == 3.6062334122200004
test()

print(output(0,float(input('Enter a value of y: '))))