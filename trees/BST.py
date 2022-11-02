class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True

        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False

            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

    def min_value_node(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value


# m1 = BinarySearchTree()
# m1.insert(2)
# m1.insert(1)
# m1.insert(3)
# print(m1.root.value)
# print(m1.root.left.value)
# print(m1.root.right.value)


# m1 = BinarySearchTree()
# m1.insert(50)
# m1.insert(20)
# m1.insert(30)
# m1.insert(60)
# m1.insert(70)
# m1.insert(40)
# m1.insert(80)
# # print(m1.contains(90))
# # print(m1.contains(30))


# print(m1.min_value_node(m1.root))
# print(m1.min_value_node(m1.root.right))
