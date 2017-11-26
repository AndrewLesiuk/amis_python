def recnumberint(n, vvid):
    if vvid == 0:
        n = input("Введіть число N: ")
    if n.isdigit() is False:
        print("Помилка! Невірне значення")
        vvid = 0
        return(recnumberint(n, vvid))
    else:
        return(n)


def poisk(k, n, iterator):
    if k*k < n:
        k = iterator
        return(poisk(k, n, iterator+1))
    else:
        return(k)
print('Програма знаходить найменьше ціле число K, квадрат якого більше N')
vvid = 0
n = 0
iterator = 0
k = 1
n = int(recnumberint(n, vvid))
k = poisk(k, n, iterator)
print(n, "<", k**2)
print("K =", k)
