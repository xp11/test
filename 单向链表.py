class SingleNode:
    def __init__(self,val,next = None,prev = None):
        self.val = val
        self.next = next
        self.prev = prev
    def __repr__(self):
        return str(self.val)
    # def __str__(self):
    #     return str(self.val)

class LinkList:
    def __init__(self):
        self.nodes = []
        self.head = None
        self.tail = None

    # def __len__(self):
    #     return len(self.nodes)

    def __getitem__(self, item):
        return self.nodes[item]

    def append(self, val):
        node = SingleNode(val)
        prev = self.tail
        if prev is None:
            self.head = node
        else:
            prev.next = node
        self.nodes.append(val)
        self.tail = node

    def iternodes(self, reverse=False):
        current = self.head
        while current:
            yield current
            current = current.next

ll = LinkList()
ll.append(5)
ll.append(88)
ll.append(1)
ll.append(23)
for node in ll.iternodes():
    print(node)


