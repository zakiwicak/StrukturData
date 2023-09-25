class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def filter_omoer(self):
        ayam_dewasa = []

        current = self.head
        while current:
            umur = current.data

            if umur >= 300 and umur <= 600:
                ayam_dewasa.append(umur)

            current = current.next

        return ayam_dewasa


# Test case
Arr = [507, 20, 241, 178, 3, 257, 488, 582, 357, 55,
       419, 480, 232, 588, 362, 393, 115, 133, 509, 218]

linked_list = LinkedList()

for umur in Arr:
    linked_list.insert(umur)

ayam_dewasa = linked_list.filter_omoer()
print(ayam_dewasa)
