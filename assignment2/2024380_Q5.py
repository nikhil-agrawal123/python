def float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

cx = float_input("Enter scaling parameter cx: ")
cy = float_input("Enter scaling parameter cy: ")

scaling_matrix = [[cx,0,0],[0,cy,0],[0,0,1]]

def original_matrix():
    matrix = []
    for _ in range(3):
        while True:
            try:
                x, y = map(int, input('Enter space-separated x, y: ').split())
                matrix.append([x, y, 1])
                break
            except ValueError:
                print("Invalid input. Please enter two space-separated integers.")
    return matrix

def matrx_scaling(matrix,sclaing_matrix):
    out = []
    for i in range(3):
        sum = 0
        new = []
        for k in range(3):
            sum += matrix[i][k] * sclaing_matrix[k][k]
            new.append(sum)
            sum = 0
        out.append(new)
    return out

def output(out):
    new_out = []
    for i in range(3):
        inner = []
        for j in range(3):
            inner.append(out[j][i])
        new_out.append(inner)
    return new_out[:2]

print(output(matrx_scaling(original_matrix(),scaling_matrix)))

def test():
    assert matrx_scaling([[1, 2, 1], [1, 2, 1], [1, 2, 1]],[[2,0,0],[0,2,0],[0,0,1]]) == [[2.0, 4.0, 1], [2.0,4.0, 1], [2.0,4.0, 1]]

test()