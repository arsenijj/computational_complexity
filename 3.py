def polynom_view(coefficients, flag=0):
    polynom = [f'{coefficient}x^{num+1}' for num, coefficient in enumerate(coefficients[1:])]
    polynom.append(coefficients[0])

    if flag == 1:
        print('(', end='')
        print(*polynom, sep=' + ', end=') * ')
    elif flag == 2:
        print('(', end='')
        print(*polynom, sep=' + ', end=') = ')
    else:
        print(*polynom, sep=' + ')
    return


def multiplication(n, a, m, b, res):
    for i in range(n):
        for j in range(m):
            res[i+j] += a[i] * b[j]
    return res


def get_data():
    print('Введите размер полинома:')
    size = int(input())
    print(f'Введите коэффициенты у членов полинома (всего {size}), начиная со степени 0:')
    # polynom = [int(input()) for _ in range(size)]
    polynom = [int(value) for value in input().split()]
    return size, polynom


print('Введите первый полином:')
n, a = get_data()

print('Введите второй полином:')
m, b = get_data()

if n < m:
    n, m = m, n
    a, b = b, a
res = [0 for _ in range(n + m - 1)]

polynom_view(a, 1)
polynom_view(b, 2)
polynom_view(multiplication(n, a, m, b, res))
