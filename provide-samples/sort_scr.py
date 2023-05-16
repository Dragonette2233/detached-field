d = {"a": 34, "b": 66, "c": 12, "d": 9000}


def get_two_higher(obj: dict):
    sorted_tuple = sorted(obj.items(), key=lambda k: k[1], reverse=True)
    return (sorted_tuple[0][1], sorted_tuple[1][1])


print(get_two_higher(d))