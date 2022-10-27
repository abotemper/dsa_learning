
# 必须先建立一个node类，每个node有两个properties，一个是value，一个是next，next用于寻找下一个节点，
# 初始时必须为None
# 之后再正式写一个链表类，首先建立新链表类的时候，通过传入的value，可以先建立一个节点，此外
# 还包括一个头，一个尾，他们都等于上述建立的节点，其含义是这两个东西都指向这个节点，
# 最后一个元素是链表长，初始化为1
# 这其中包括的方法有，打印，从后加入新节点，从后pop一个节点，前加，前删，get，set
# 插入，删除，逆转这一系列方法


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

# 打印链表，设想链表不空的时候，先创建一个临时的指针变量，这个指针最先指向头的位置，当指向不空时，打印这个指针指向元素的value
# 之后让指针指向原本元素的next元素
    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            print('------------------------------')
            temp = temp.next

# 后加方法，首先根据传值新建立一个节点，如果头指向为空，则让头尾都指向这个新节点
# 如果头指向不空则让尾指向元素的next指向新节点，然后重新让尾指向新节点
# 最后让链表长自加一，返回true
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

# 后出方法，如果链表为空则返回空
# 反之，则创建两个新的指针，A指向头，B指向尾，如果A指向元素的下一个元素不空时，让B先指向A，然后A指向下一个元素
# 这样的原因是为了找到最后一个元素。
# 当A指向元素的下一个元素为空时就停止了，A也就指向了最后一个元素
# 先让尾向前移到B的位置，也就是最后一个元素的前一个元素上，让尾的next指向空，这样就把最后一个元素从链表中断开了，
# 但是我们还能通过A找到最后一个元素，在让链表长减一，如果长为0时，让头尾都指向空，返回则返回给A，这样断开了最后一个元素，同时还能把他pop出来
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.tail
        while (temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

# 前加方法，先通过传入的参数建立一个新节点，如果链表还是空的，那么就让头尾都指向这个新节点
# 如果不空则，让新的节点的next指向头元素，在把头元素前移，指向这个新元素，链表长加一，返回true
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

# 前出方法，当链表为空时返回空，否则则创建一个新的临时指针指向头元素，这是因为我们要动头，防止我们动了之后找不见原来的头元素
# 然后将头向后移，指向原来的next元素，然后原来的头的next指向空，这样就断开了，
# 长度减一，当长减完为0时，我们需要把尾元素置空，最后返回这个元素，头指针在过程中已经会指向空了
    def popFirst(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

# get方法，当给的参数不合法时返回空，合法时我们需要根据参数从头向后找，因为是get，不动链表，头尾都不动
# 建立一个临时指针指向头元素，然后再0-index之间进行遍历，让临时指针一直向后走，走动最后那就是index对应的值，
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
    # _ 的意思是在函数里用不上
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

# set方法，意图把index上的值改成想要的值，创建一个临时指针，直接使用上面的get方法找到那个元素
# 当这个元素不空时，将它的value改了，如果为空则返回false
    def set(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

# 插入方法，如果index不合法则返回false，如果index为0则问题退化成前加，如果index为最后一个元素时，问题退化成后加
# 如果在中间时，那么就需要先根据传入的value创建一个新节点，让一个指针指向index的前一个元素，让新元素的next指向index这个元素
# 然后让前一个元素的next指向新的元素，长度加一，返回正确
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        newNode = Node(value)
        temp = self.get(index - 1)
        newNode.next = temp.next
        temp.next = newNode
        self.length += 1
        return True

# 删除方法，如果index不合法，那么返回空，如过index为0那么退化成前出方法，如果index为最后一个元素，则问题退化为后出
# 如果在中间我们需要两个新指针，第一个A指向index的前一个元素，另一个B指向index
# 让B指向A的后一个元素而不是A的指向，让A指向为空，相当于直接把链表断开，又重新连接，把这个元素拿掉，最后返回这个元素
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.popFirst()
        if index == self.length - 1:
            return self.pop()

        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

# 逆转链表，首先一个临时指针指向头元素，用以对调头尾指向，
# 再建立两个临时指针A和B， A先指向原头元素的下一个元素，B指向原头元素的前一个，其实现在来说是空
# 遍历整个链表，让A指向原头元素的下一个元素，然后头元素的next不再指向后一个元素，而是指向前面的元素也就是B指向的空
# 这样头元素就成了最后一个元素了，然后将B指针向后移，移到头元素的位置，相当于也向后走了一步，然后temp再往后走一步
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


m3 = LinkedList(0)
m3.append(1)
m3.append(2)
m3.append(3)

m3.reverse()
m3.printList()
