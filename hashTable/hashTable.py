class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
            return my_hash

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

# m1 = HashTable()
# m1.set_item('gg', 200)
# m1.set_item('hh', 300)
# m1.set_item('as', 400)
# m1.set_item('qw', 500)
# m1.set_item('zx', 600)

# m1.print_table()


# m1 = HashTable()
# m1.set_item('gg', 200)
# m1.set_item('hh', 300)
# m1.set_item('as', 400)
# m1.set_item('qw', 500)
# m1.set_item('zx', 600)

# print(m1.get_item("hh"))
# print(m1.get_item("as"))
# print(m1.get_item("gw"))
# print(m1.get_item("qw"))
