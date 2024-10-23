def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def month_number(month):
    if month == 'january':
        return 1
    elif month == 'feburary':
        return 2
    elif month == 'march':
        return 3
    elif month == 'april':
        return 4
    elif month == 'may':
        return 5
    elif month == 'june':
        return 6
    elif month == 'july':
        return 7
    elif month == 'august':
        return 8
    elif month == 'september':
        return 9
    elif month == 'october':
        return 10
    elif month == 'november':
        return 11
    else:
        return 12

def reverse_month_number(month):
    if month == 1:
        return 'january'
    elif month == 2:
        return 'feburary'
    elif month == 3:
        return 'march'
    elif month == 4:
        return 'april'
    elif month == 5:
        return 'may'
    elif month == 6:
        return 'june'
    elif month == 7:
        return 'july'
    elif month == 8:
        return 'august'
    elif month == 9:
        return 'september'
    elif month == 10:
        return 'october'
    elif month == 11:
        return 'november'
    else:
        return 'december'

def month_day(month, year):
    if month == 'january' or month == 'march' or month == 'may' or month=='july' or month=='august' or month =='october' or month=='december':
        return 31
    elif month == 'feburary':
        if leap_year(year):
            return 29
        else:
            return 28
    else:
        return 30

def day_of_week(day, month, year):
    if year < 0:
        year = ((year)*(-1) - 1)*-1

    if month < 3:
        month += 12
        year -= 1
    return (day + 13 * (month + 1) // 5 + year % 100 + (year % 100) // 4 + year // 400 + 5 * (year // 100)) % 7
#direct formula of calculation taken from wikipedia zeller's formula

def print_calendar(month, year):
    print('Mon Tue Wed Thu Fri Sat Sun')
 
    start = (day_of_week(1, month, year) + 5) % 7

    print('    ' * start, end='')

    for day in range(1, (month_day(reverse_month_number(month), year)) + 1):
        print(f'{day:3}', end=' ')
        if (day + start) % 7 == 0:
            print()
    print()

input_month = input('enter month ')
number = month_number(input_month)
input_year = int(input('enter year (for bc input negativce year) '))
print_calendar(number, input_year)

while True:
    z = input('next/previous/exit ')
    if z == 'next':
        number+=1
        print_calendar(number, input_year)
    if z == 'previous':
        number-=1
        print_calendar(number, input_year)
    if z == 'exit':
        break