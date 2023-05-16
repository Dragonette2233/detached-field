class HashTable:
    def __init__(self):
        self.size = 10  # размер таблицы
        self.table = [[] for _ in range(self.size)]  # создаем пустые списки для каждой ячейки

    def __hash_function(self, key):  # хэш-функция, которая возвращает индекс ячейки
        return hash(key) % self.size

    def insert(self, key, value):  # метод для вставки новой пары ключ-значение
        idx = self.__hash_function(key)  # получаем индекс ячейки
        for item in self.table[idx]:  # проверяем, есть ли уже такой ключ в ячейке
            if item[0] == key:
                item[1] = value  # обновляем значение
                return
        self.table[idx].append([key, value])  # добавляем новую пару

    def search(self, key):  # метод для поиска значения по ключу
        idx = self.__hash_function(key)  # получаем индекс ячейки
        for item in self.table[idx]:
            if item[0] == key:
                return item[1]
        raise KeyError('Key not found: {}'.format(key))  # если ключ не найден, выбрасываем исключение

    def remove(self, key):  # метод для удаления пары ключ-значение
        idx = self.__hash_function(key)  # получаем индекс ячейки
        for i, item in enumerate(self.table[idx]):
            if item[0] == key:
                del self.table[idx][i]  # удаляем пару
                return
        raise KeyError('Key not found: {}'.format(key))  # если ключ не найден, выбрасываем исключение
    

ht = HashTable()
ht.insert('John', 28)
ht.insert('Jane', 35)
print(ht.search('John'))  # выводит 28
ht.remove('Jane')
print(ht.table)