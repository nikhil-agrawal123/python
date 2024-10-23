x,y=map(int,input('give space seperated 2 values').split())

def reverse(x,y):
    c = 0
    d = x
    while d > 0:
        d = d//10
        c += 1 #found length of the number

    q = x//(10**(c-y))
    r = x%(10**(c-y))
    r_new = r*(10**y) + q

    return r_new,c


def even_odd_sum(x,y):
    even_sum = 0
    odd_sum = 0
    
    z,y = reverse(x,y)
    for i in range(1,y+1):
        if i%2 == 0:
            even_sum += z%10
            z = z//10
        else:
            odd_sum += z%10
            z = z//10
    
    if odd_sum <= even_sum:
        return f'{x} is the lucky number'
    else:
        return f'{x-1} is the lucky number'

def test():
    assert reverse(1234,2) == (3412,4)
    assert reverse(1234,1) == (4123,4)
    assert even_odd_sum(1234,2) == '1234 is the lucky number'
    assert even_odd_sum(1234,1) == '1233 is the lucky number'
test()

print(even_odd_sum(x,y))