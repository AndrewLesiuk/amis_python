def recfactorial(x, n, p):
    if n < 2:
        return p+x
    else:
        p = p+x**n
        return(recfactorial(x, n-1, p))


def recnumberfloat(x, vvid):
    if vvid == 0:
        x = input("Введіть число x: ")
    if x.lstrip('-').replace('.', '', 1).isdigit() is False:
        print("Помилка! Невірне значення")
        vvid = 0
        return(recnumberfloat(x, vvid))
    else:
        return(x)


def recnumberint(n, vvid1):
    if vvid1 == 0:
        n = input("Введіть число n: ")
    if n.isdigit() is False:
        print("Помилка! Невірне значення")
        vvid = 0
        return(recnumberint(n, vvid1))
    else:
        return(n)
p = 0
vvid = 0
x = 0
vvid1 = 0
n = 0
print("Програма вирішує рівняння х**і від і=1 до n")
x = float(recnumberfloat(x, vvid))
n = int(recnumberint(n, vvid1))
print("Резутат", recfactorial(x, n, p))
