class Node:
    def __init__(self, previous_node, next_node, key, value):
        self.previous_node = previous_node
        self.next_node = next_node
        self.value = value
        self.key = key


class DoubleLinkedList:

    # tail will always have the latest element
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # O(1)
    def add_element(self, key, value) -> Node:
        # empty list
        if not self.head:
            new_node = Node(None, None, key, value)
            self.tail = new_node
            self.head = new_node
        else:
            last_node = self.tail
            new_node = Node(last_node, None, key, value)
            last_node.next_node = new_node
            self.tail = new_node
        self.length += 1
        return new_node

    # O(1)
    def delete_node(self, node: Node):
        previous_node: Node = node.previous_node
        next_node: Node = node.next_node
        if previous_node:
            previous_node.next_node = next_node
        else:
            self.head = next_node
        if next_node:
            next_node.previous_node = previous_node
        else:
            self.tail = previous_node
        self.length -= 1
        return node

    # O(1)
    def delete_oldest(self) -> Node:
        oldest_node: Node = self.head
        print("discarding: {}-{}".format(oldest_node.key, oldest_node.value))
        self.delete_node(oldest_node)
        return oldest_node

    def get_tail(self) -> Node:
        return self.tail

    def get_head(self) -> Node:
        return self.head

    # O(n)
    def print_list(self):
        current_node: Node = self.head
        while current_node:
            print("{} {}".format(current_node.key, current_node.value))
            current_node = current_node.next_node
        print("-----------------")

    # O(1)
    def get_length(self):
        return self.length
