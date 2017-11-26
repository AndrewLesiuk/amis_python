def recnumberint(n, vvid1, iterator):
    if vvid1 == 0:
        n = input(list())
    n1 = n.split(" ")
    if n == "":
        print("Помилка! Невірне значення")
        vvid1 = 0
        return(recnumberint(n, vvid1, iterator))
    elif iterator == len(n1):
        spisokreverce = n[::-1]
        return(spisokreverce)
    elif n1[iterator].isdigit() is False:
        print("Помилка! Невірне значення")
        vvid1 = 0
        iterator = 0
        return(recnumberint(n, vvid1, iterator))
    else:
        vvid1 = 1
        return(recnumberint(n, vvid1, iterator+1))
print("Програма виводить список у зворотньому порядку")
vvid1 = 0
n = 0
iterator = 0
spisok = recnumberint(n, vvid1, iterator)
print(spisok)
