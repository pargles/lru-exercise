from src.DoubleLinkedList import DoubleLinkedList


def test_initialization():
    dll: DoubleLinkedList = DoubleLinkedList()
    assert dll.head is None
    assert dll.tail is None


def test_empty_after_removing_elements():
    dll: DoubleLinkedList = DoubleLinkedList()
    dll.add_element("1", "bananas")
    dll.delete_oldest()
    assert dll.head is None
    assert dll.tail is None


def test_empty_then_add_element():
    dll: DoubleLinkedList = DoubleLinkedList()
    dll.add_element("1", "bananas")
    dll.delete_oldest()
    node = dll.add_element("2", "apples")
    assert dll.head == node
    assert dll.tail == node
    assert dll.get_length() == 1


def test_delete_oldest():
    dll: DoubleLinkedList = DoubleLinkedList()
    oldest_value: str = "bananas"
    dll.add_element("1", oldest_value)
    dll.add_element("2", "strawberries")
    dll.add_element("3", "mangos")
    oldest = dll.delete_oldest()
    assert oldest.value == oldest_value


def test_delete_head_node():
    dll: DoubleLinkedList = DoubleLinkedList()
    first_head_node = dll.add_element("1", "bananas")
    expected_head_node = dll.add_element("2", "strawberries")
    dll.add_element("3", "mangos")
    dll.delete_node(first_head_node)
    assert dll.head == expected_head_node
    assert dll.get_length() == 2


def test_delete_tail_node():
    dll: DoubleLinkedList = DoubleLinkedList()
    dll.add_element("1", "bananas")
    expected_tail_node = dll.add_element("2", "strawberries")
    last_tail_node = dll.add_element("3", "mangos")
    dll.delete_node(last_tail_node)
    assert dll.tail == expected_tail_node
    assert dll.get_length() == 2


def test_delete_node_in_the_middle():
    dll: DoubleLinkedList = DoubleLinkedList()
    expected_head_node = dll.add_element("1", "bananas")
    node_to_be_deleted = dll.add_element("2", "strawberries")
    expected_tail_node = dll.add_element("3", "mangos")
    dll.delete_node(node_to_be_deleted)
    assert dll.head == expected_head_node
    assert dll.tail == expected_tail_node
    assert dll.get_length() == 2
