def recnumberint(n, vvid1, iterator):
    if vvid1 == 0:
        n = input(list())
    n1 = n.split(" ")
    if n == "":
        print("Помилка! Невірне значення")
        vvid1 = 0
        return(recnumberint(n, vvid1, iterator))
    elif len(n1) < 2:
        print("Помилка! Невірне значення")
        vvid1 = 0
        return(recnumberint(n, vvid1, iterator))
    elif iterator == len(n1):
        return(n)
    elif n1[iterator].isdigit() is False:
        print("Помилка! Невірне значення")
        vvid1 = 0
        iterator = 0
        return(recnumberint(n, vvid1, iterator))
    else:
        vvid1 = 1
        return(recnumberint(n, vvid1, iterator+1))


def recmaxx(n, maxx, maxx1, iterator1):
    n1 = n.split(" ")
    if iterator1 <= len(n1)-1:
        if int(n1[iterator1]) >= int(maxx):
            maxx1 = maxx
            maxx = n1[iterator1]
            return(recmaxx(n, maxx, maxx1, iterator1+1))
        else:
            return(recmaxx(n, maxx, maxx1, iterator1+1))
    else:
        return(maxx1)
print("Програма знаходить другий максимальний елемент")
vvid1 = 0
n = 0
iterator = 0
iterator1 = 0
n = recnumberint(n, vvid1, iterator)
n1 = n.split(" ")
maxx = n1[iterator1]
maxx1 = n1[iterator1]
print("Другий максимальний елемент =", recmaxx(n, maxx, maxx1, iterator1))
