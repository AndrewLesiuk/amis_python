def power(a, n):
    if n == 0:
        return 1
    else:
        return power(a, n-1) * a
print("Програма рахує степінь числа a")
a = float(input("Введіть число а:"))
n = float(input("Введіть степінь числа а:"))
print("Результат:", power(a, n))
