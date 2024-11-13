def is_prime(n):
    def wrapper():
        res = 0
        if n < 1:
            res = (f"Число {n} является составным.")
        if n == 2:
            res = (f"Число {n} является простым.")
        if n % 2 == 0:
            res = (f"Число {n} является составным.")
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                res = (f"Число {n} является составным.")
            else:
                res = (f"Число {n} является простым.")
        return res
    return wrapper()


def sum_tree(*args):
    sum_ = sum(args)
    print(sum_)
    return sum_



result = is_prime(sum_tree(2, 3, 6))
print(result)
