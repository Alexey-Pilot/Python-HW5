def sum_nums(num1, num2):
    if num1 == 0 and num2 == 0:
        return 0
    elif num1 == 0:
        return 1 + sum_nums((num1, num2 - 1))
    elif num2 == 0:
        return 1 + sum_nums(num1 - 1, num2)
    return  2 + sum_nums(num1 - 1, num2 - 1)

n, m = [int(input("Введите число: ")) for _ in range(2)]
print(sum_nums(n, m))