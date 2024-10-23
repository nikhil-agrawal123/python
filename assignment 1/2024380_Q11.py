def side_view(x): #finally spacing ki galti sahi kar di :)
    for i in range(1,x+1):
        print(" "*(2*(x-i))+"*"*(4*i-3))	
        print()


def top_view(x): #discussed with sifat from section B
    size = 4*x-3
    if x%2 == 0:
        for i in range(size):
            for j in range(size):
                a = x - min(i ,size-1-i,j, size-1-j)
                if a%2 ==0 :
                    print('*',end=' ')
                else:
                    print(' ',end=' ')
            print()
    else:
        for i in range(size):
            for j in range(size):
                a = x - min(i ,size-1-i,j, size-1-j)
                if a%2 !=0 :
                    print('*',end=' ')
                else:
                    print(' ',end=' ')
            print()

x = int(input("Enter the number of rows: "))
while True:
    a = 'side_view'
    if a == 'side_view':
        z = x
        side_view(z)
        y = input("Do you want to see the top view? (y/n): ")
        if y == 'y':
            a = 'top_view'
        else:
            break
    if a == 'top_view':
        top_view(z)
        y = input("Do you want to see the side view? (y/n): ")
        if y == 'y':
            a = 'side_view'
        else:
            break