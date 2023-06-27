class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node data: {self.data}"


class Linked_List:
    def __init__(self):
        self.head = None

    def add_tail(self, data):
        node = Node(data)

        if (self.head == None):
            self.head = node
            return
        else:
            current = self.head
            while (current.next):
                current = current.next
            current.next = node

    def add_head(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def __repr__(self) -> str:
        nodes = []
        current = self.head
        while (current):
            nodes.append(f"{current.data}")
            current = current.next
        return "->".join(nodes)


lk = Linked_List()
lk.add_head(20)
lk.add_head(50)
lk.add_head(30)
lk.add_tail(50)
lk.add_tail(100)
print(lk)
