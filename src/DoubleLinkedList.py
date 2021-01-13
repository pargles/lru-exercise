class Node:
    def __init__(self, previous_node, next_node, key, value):
        self.previous_node = previous_node
        self.next_node = next_node
        self.value = value
        self.key = key


class DoubleLinkedList:

    # tail will always have the latest element
    def __init__(self):
        self.tail = None
        self.head = None

    #O(1)
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
        return node

    # O(1)
    def delete_oldest(self) -> Node:
        oldest_node: Node = self.head
        print("discarding: {}".format(oldest_node.value))
        self.delete_node(oldest_node)
        return oldest_node

    def get_tail(self) -> Node:
        return self.tail

    def get_head(self) -> Node:
        return self.head

    #O(n)
    def print_list(self):
        current_node: Node = self.head
        while current_node:
            previous_value = current_node.previous_node.value if current_node.previous_node else None
            next_value = current_node.next_node.value if current_node.next_node else None
            current_value = current_node.value
            print("{} <- {} -> {} ".format(previous_value, current_value, next_value))
            current_node = current_node.next_node
        print("-----------------")

    # O(n)
    def get_length(self):
        current_node: Node = self.head
        counter = 0
        while current_node:
            current_node = current_node.next_node
            counter += 1
        return counter


if __name__ == "__main__":
    # list = DoubleLinkedList()
    # some_text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry".split(" ")
    # for word in some_text:
    #     list.add_element(word)
    # # list.print_list()
    # list.delete_oldest()
    # list.delete_oldest()
    # print("---------------")
    # # list.print_list()
    dll: DoubleLinkedList = DoubleLinkedList()
    expected_head_node = dll.add_element("1", "bananas")
    node_to_be_deleted = dll.add_element("2", "strawberries")
    expected_tail_node = dll.add_element("3", "mangos")
    dll.delete_node(node_to_be_deleted)
    assert dll.head == expected_head_node
    assert dll.tail == expected_tail_node
    assert dll.get_length() == 2