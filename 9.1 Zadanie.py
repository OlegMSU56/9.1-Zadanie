def apply_all_func(int_list, *functions):
    results = {}
    for function in functions:
        a = function(int_list)
        results.setdefault(function. __name__, [a])
    return results


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))