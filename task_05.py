def get_matrix(n, m, value):
    matrix = []
    for _ in range(n):
        matrix.append([])
    for i in range(m):
        for k in range(n):
            matrix[k].append(value)
    print(matrix)
    return matrix

result1 = get_matrix(5,3,11)
result2 = get_matrix(2,4,22)
result3 = get_matrix(6,2,33)


