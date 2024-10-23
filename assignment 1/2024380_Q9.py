import random

def direction():
    direction = ''
    a = random.randint(0,1)
    if a == 0:
        direction = 'x'
    else:
        direction = 'y'

    return direction

def random_steps(final_x,final_y):
    x = 0
    y = 0
    total_steps = 0
    while x<final_x or y < final_y:
        direction_move = direction()

        if x == final_x:
            direction_move = 'y'
        if y == final_y:
            direction_move = 'x'

        d = random.randint(0,5)

        if direction_move == 'x':
            x += d
            if x > final_x:
                x = final_x

        if direction_move == 'y':
            y += d
            if y > final_y:
                y = final_y
        total_steps +=1
    return total_steps


def output(x,y):
    total_steps = 0
    walks = 0
    avg1 = 0

    while True:
        total_steps += random_steps(x,y)
        walks += 1

        avg2 = total_steps/walks
        if walks> 1:
            if abs(avg1-avg2)/avg1 < 0.1:
                return avg2,walks
        avg1 = avg2

x,y = map(int,input('Enter space sepeterated final x and y coordinates').split())  
print(output(x,y))