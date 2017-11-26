def recnumberint(n, vvid1, iterator):
    if vvid1 == 0:
        n = input(list())
    n1 = n.split(" ")
    if n == "":
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


def recmin(n, minn, iterator1):
    n1 = n.split(" ")
    if iterator1 <= len(n1)-1:
        if int(n1[iterator1]) <= int(minn):
            minn = n1[iterator1]
            return(recmin(n, minn, iterator1+1))
        else:
            return(recmin(n, minn, iterator1+1))
    else:
        return(minn)
print("Програма знаходить мінімальний елемент")
vvid1 = 0
n = 0
iterator = 0
iterator1 = 0
n = recnumberint(n, vvid1, iterator)
n1 = n.split(" ")
minn = n1[iterator1]
print("Mінімальний елемент =", recmin(n, minn, iterator1))
