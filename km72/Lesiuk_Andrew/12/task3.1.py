def recnumberint(n, vvid1, iterator):
    if vvid1 == 0:
        n = input(list())
    n1 = n.split(" ")
    if n == "":
        print("Помилка! Невірне значення")
        vvid1 = 0
        return(recnumberint(n, vvid1, iterator))
    elif len(n1) < 1:
        print("Помилка! Елементів має бути більше")
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


def recmaxx(n, maxx, k, elem, elemm, iterator1):
    n1 = n.split(" ")
    if iterator1 <= len(n1)-1: 
        if int(n1[iterator1-1]) == int(n1[iterator1]):
            k = k+1
            elem = n1[iterator1]
        else:
            k = 1 
        if int(k) > int(maxx):
            maxx = k
            elemm = n1[iterator1]           
        return(recmaxx(n, maxx, k, elem, elemm, iterator1+1))
    else:
        return(maxx, elemm*maxx)
print("Програма визначає, яка найбільша кількість однакових\
елементів в одній групі")
elemm = 0
elem = 0
k = 0
vvid1 = 0
n = 0
iterator = 0
iterator1 = 0
n = recnumberint(n, vvid1, iterator)
n1 = n.split(" ")
maxx = 1
print("Відповідь", recmaxx(n, maxx, k, elem, elemm, iterator1))
