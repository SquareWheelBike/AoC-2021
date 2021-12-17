from os import getcwd


# got chinese remainder from https://medium.com/analytics-vidhya/chinese-remainder-theorem-using-python-25f051e391fc
from functools import reduce
def chinese_remainder(m, a):
    sum = 0
    prod = reduce(lambda acc, b: acc*b, m)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


def main():
    with open(f"{getcwd()}/2020/day13/input.txt", "r") as file:
        file = file.readlines()
    busses = list(file[1].split(","))

    a = []
    n = []
    for i, x in enumerate(busses):
        if x == "x":
            continue

        x = int(x)
        a.append(x - i % x)
        n.append(x)

    print(chinese_remainder(n, a))


if __name__ == "__main__":
    main()
