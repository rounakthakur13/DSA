class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Linked:
    def __init__(self):
        self.head = None
    def show(self):
        node = self.head
        while node is not None:
            print(node.data, end='->')
            node = node.next
    def add(self, new):
        new_node = Node(new)
        new_node.next = self.head
        self.head = new_node
link = Linked()
elem = Node('Rounak')
link.head = elem
elem2 = Node('Lalit')
link.head.next = elem2
link.add("Hello")
print(link.show())