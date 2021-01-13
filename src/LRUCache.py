from src.DoubleLinkedList import DoubleLinkedList, Node


class LRUCache:

    def __init__(self, max_items: int):
        self.max_size = max_items
        self.reset()

    # O(1)
    def get(self, key: str):
        current_value: Node = self.cache.get(key, None)
        if current_value:
            self.put(key, current_value.value)
            return current_value.value
        return current_value

    # O(1)
    def put(self, key: str, value):
        # safe access to map, return None if key doesn't exist
        current_element: Node = self.cache.get(key, None)
        if current_element:
            self.array.delete_node(current_element)
            self.current_size -= 1
        elif self.current_size >= self.max_size:
            oldest_node = self.array.delete_oldest()
            # store the key?
            del self.cache[oldest_node.key]
        # adding to the tail of the list
        new_node: Node = self.array.add_element(key, value)
        self.cache[key] = new_node
        self.current_size += 1

    # O(1)
    # method cannot be called del because it's a reserved word in python
    def delete(self, key: str):
        current_element: Node = self.cache.get(key, None)
        if current_element:
            del self.cache[key]
            self.array.delete_node(current_element)
            self.current_size -= 1

    # O(1)
    def reset(self):
        self.cache = {}
        self.current_size = 0
        self.array: DoubleLinkedList = DoubleLinkedList()

    def print_cache(self):
        self.array.print_list()


if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put("1", "bananas")
    cache.put("2", "apples")
    cache.put("3", "strawberry")
    cache.put("4", "pineapple")
    cache.put("3", "strawberry")
    cache.print_cache()
