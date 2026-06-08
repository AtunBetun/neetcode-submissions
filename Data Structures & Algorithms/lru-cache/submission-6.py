class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = Node(0, 0)  # Dummy head
        self.tail = Node(0, 0)  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_front(self, node: Node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node: Node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def move_to_front(self, node: Node):
        self.remove_node(node)
        self.add_front(node)

    def remove_tail(self) -> Node:
        last = self.tail.prev
        self.remove_node(last)
        return last

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> Node
        self.dll = DoubleLinkedList()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.dll.move_to_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.dll.move_to_front(node)
        else:
            if len(self.cache) == self.capacity:
                last = self.dll.remove_tail()
                del self.cache[last.key]
            new_node = Node(key, value)
            self.dll.add_front(new_node)
            self.cache[key] = new_node
