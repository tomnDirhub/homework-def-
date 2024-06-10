def get_matrix(n, m, value):
    a = list()
    for i in range(n):
        a.append([])
        for j in range(m):
            a[i].append([])
            a[i][j] = value
    return [a[i] for i in range(n)]

a = get_matrix(5, 5, '(:)')
for i in range(len(a)):
    print(a[i], sep='')