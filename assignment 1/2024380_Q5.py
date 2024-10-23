def demand(x):
    return 2.71**(10 - 1.05*x)

def supply(x):
    return 2.71**(1 + 1.06*x)

def main(x):
    price = x
    i = 1
    while i<50:
        if (demand(price)) - (supply(price)) <0.001  :
            return (price), (demand(price)), (supply(price))
        else:
            price += price*0.05	
            i +=1
    return "No such price exists"

def test():
    assert demand(0) == 2.71**10
    assert supply(0) == 2.71
    assert main(0) == "No such price exists"
test()
        
print(main(float(input('Enter price: '))))
