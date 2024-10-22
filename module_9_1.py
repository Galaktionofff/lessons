def apply_all_func(int_list: (int, float), *functions):
    results = {}
    for f in functions:
        results[f.__name__] = list(map(f, [int_list]))
    print(*results.items())
    return results


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
