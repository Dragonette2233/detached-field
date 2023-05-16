from timeit import timeit

def makelist_1():
    result = []
    for val in range(1000):
        result.append(val)
    return result

def makelist_2():
    return [val for val in range(1000)]

print(f"First way: {timeit(makelist_1, number=1000)} seconds")
print(f"Second way: {timeit(makelist_2, number=1000)} seconds")