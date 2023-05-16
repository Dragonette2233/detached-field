def superlong_sum(a: str, b: str) -> str:

    def higher(value_1, value_2) -> list:

        if len(value_1) > len(value_2):
            slice_var = len(value_1) - len(value_2)
            return value_1[:slice_var]
        else:
            slice_var = len(value_2) - len(value_1)
            return value_2[:slice_var]

    a, b = [int(i) for i in a], [int(s) for s in b]

    zipped = list(zip(a[::-1], b[::-1]))
    new_list = [sum(i) for i in zipped]
   
    for i, val in enumerate(new_list):
        if val > 9:
            try:
                new_list[i+1] += 1
            except:
                new_list.append(1)

            new_list[i] = val - 10

    new_list += higher(a, b)[::-1]
    return ''.join(str(i) for i in new_list[::-1])

first_slong =  '111'
second_slong = '111'
total_sum = slong_sum(first_slong, second_slong)

print(total_sum)