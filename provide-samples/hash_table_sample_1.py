import sys

class HashTable:

    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def __setitem__(self, key, value):
        hash_key = hash(key) % self.size
        for index, element in enumerate(self.table[hash_key]):
            if element[0] == key:
                self.table[hash_key][index] = (key, value)
                break
        else:
            self.table[hash_key].append((key, value))

    def __getitem__(self, key):
        hash_key = hash(key) % self.size
        for k, v in self.table[hash_key]:
            if k == key:
                return v
        raise KeyError(key)

    def __delitem__(self, key):
        hash_key = hash(key) % self.size
        for index, element in enumerate(self.table[hash_key]):
            if element[0] == key:
                del self.table[hash_key][index]
                return
        raise KeyError(key)
    
    def __str__(self):
        output = []
        for bucket in self.table:
            for key, value in bucket:
                if value is not None:
                    output.append(f"{key}: {value}")
        return "{" + ", ".join(output) + "}"

