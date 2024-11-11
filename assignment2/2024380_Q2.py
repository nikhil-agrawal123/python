a = []
x = list(map(str, input('Enter space-separated course number, course credits, grade received: ').split()))

while x != []:
    if not x[0].isalnum():
        print('Invalid course number input')
    elif int(x[1]) not in [1, 2, 4]:
        print('Invalid credit input')
    elif x[2] not in ['A+', 'A', 'A-', 'B', 'B-', 'C', 'C-', 'D', 'F']:
        print('Invalid grade input')
    else:
        a.append(x)
    
    x = list(map(str, input('Enter space-separated course number, course credits, grade received: ').split()))

a.sort()

def report_card(a):
    print('Report Card')
    for i in range(len(a)):
        print(f'{a[i][0]}:{a[i][2]}')

report_card(a)
def grade(grade):
    if grade == 'A+':
        return 10
    elif grade == 'A':
        return 10
    elif grade == 'A-':
        return 9
    elif grade == 'B':
        return 8
    elif grade == 'B-':
        return 7
    elif grade == 'C':
        return 6
    elif grade == 'C-':
        return 5
    elif grade == 'D':
        return 4
    elif grade == 'F':
        return 2

credits = 0
grade_points = 0

for i in range(len(a)):
    credits += int(a[i][1])
    grade_points += int(a[i][1])*grade(a[i][2])

result = grade_points/credits
print('SGPA:', '{:.2f}'.format(result))

def test():
    assert grade('A+') == 10
    assert grade('A') == 10
    assert grade('A-') == 9

test()