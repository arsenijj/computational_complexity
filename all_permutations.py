a = []


def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

current = 1

def print_permutation(current_permutation):
        global current
        print(f'{current}: ', end='')
        print(*current_permutation, sep=', ')
        current += 1


def next_set(a, n):

    j = n - 2
    while j != -1 and a[j] >= a[j+1]:
        j -= 1

    if j == -1:
        return

    k = n - 1
    while a[j] >= a[k]:
        k -= 1
    swap(a, j, k)
    l = j + 1
    r = n - 1

    while l < r:
        swap(a, l, r)
        l += 1
        r -= 1
    print_permutation(a)
    return next_set(a, n)


print('Введите количество элементов множества')
n = int(input())
print(f'Введите последовательно без пробелов n элементов')

a = sorted(list(map(lambda x: int(x), input().split())))

print('Исходное множество: ', end='')
print(*a, sep=', ')
print('Всевозможные перестановки множества:')

print_permutation(a)
next_set(a, n)
