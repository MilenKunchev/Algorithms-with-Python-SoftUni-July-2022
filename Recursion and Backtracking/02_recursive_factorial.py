def calc_factorial(num):
    if num == 1:
        return num
    return num * calc_factorial(num - 1)


number = int(input())
print(calc_factorial(number))
