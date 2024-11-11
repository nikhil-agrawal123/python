def read_file():
    with open("Q3.txt", "r") as file:
        yearbook = {}
        current_student = ''
        for line in file:
            line = line.strip()
            if line.endswith(':'):
                current_student = line[:-1]
                yearbook[current_student] = {}
            else:
                name, status = line.split(', ')
                yearbook[current_student][name] = int(status)
    return yearbook
    
def sign_value(yearbook):
    new_book = {}
    for i in yearbook:
        new_book[i] =0
        for j in yearbook[i]:
            if yearbook[i][j] == 1:
                new_book[i]+= 1
    return new_book

def main(new_book):
    output_max = []
    output_min = []
    for i,j in new_book.items():
        if j == max(new_book.values()):
            output_max.append(i)
        if j == min(new_book.values()):
            output_min.append(i)
    return output_max, output_min

a,b = main(sign_value(read_file()))

print(f'Students with most signatures: {a}, Students with least signatures: {b}')

def test():
    assert read_file() == {'Alice': {'Bob': 1, 'Charlie': 0, 'David': 1}, 'Bob': {'Alice': 0, 'Charlie': 1, 'David': 0}, 'Charlie': {'Alice': 1, 'Bob': 1, 'David': 0}, 'David': {'Alice': 0, 'Bob': 0, 'Charlie': 1}}
    assert sign_value(read_file()) == {'Alice': 2, 'Bob': 1, 'Charlie': 2, 'David': 1}
    assert main(sign_value(read_file())) == (['Alice', 'Charlie'], ['Bob','David'])

test()