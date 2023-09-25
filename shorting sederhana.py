class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def print(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def sort(self):
        if not self.head or not self.head.next:
            return self.head
        else:
            current = self.head
            while current.next:
                next = current.next
                while next:
                    if current.value > next.value:
                        temp = current.value
                        current.value = next.value
                        next.value = temp
                    next = next.next
                current = current.next


# input nomor / datanya
my_linked_list = LinkedList()
my_linked_list.add(7)
my_linked_list.add(3)
my_linked_list.add(9)

print("===nomor acak awal===")
my_linked_list.print()

# panggil untuk memproses
my_linked_list.sort()

print("===data nomor setelah diurutkan===")
my_linked_list.print()
