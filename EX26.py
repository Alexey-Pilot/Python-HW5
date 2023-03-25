
def to_degree(n, m):
    if m == 0:
        return 1
    return n * to_degree(n, m - 1)

num, degree = int(input("Введите число:")), int(input("Введите степень числа: "))
print(to_degree(num, degree))