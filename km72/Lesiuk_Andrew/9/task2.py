def power(a, n):
    if n < 0:
        a = 1.0/a
        n = -n
    res = 1
    while n > 0:
        res = res * a
        n = n-1
    return res
print("Програма рахує степінь числа a")
a = float(input("Введіть число а:"))
n = float(input("Введіть степінь числа а:"))
print("Результат:", power(a, n))
