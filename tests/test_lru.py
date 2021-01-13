from src.LRUCache import LRUCache

def test_small_capacity():
    expected_length = 2
    lru = LRUCache(expected_length)
    lru.put("1", "bananas")
    lru.put("2", "pineapple")
    lru.put("3", "kiwi")
    assert len(lru.cache) == expected_length
    assert lru.array.get_length() == expected_length


def test_delete():
    lru = LRUCache(3)
    lru.put("1", "bananas")
    lru.delete("1")
    assert len(lru.cache) == 0
    assert lru.array.get_length() == 0


def test_invert_positions_on_get():
    lru = LRUCache(2)
    lru.put("1", "bananas")
    lru.put("2", "blueberries")
    lru.get("1")
    assert len(lru.cache) == 2
    assert lru.array.get_length() == 2
    assert lru.array.head.key == "2"


def test_get_no_op_for_invalid_key():
    lru = LRUCache(2)
    lru.put("1", "bananas")
    lru.put("2", "blueberries")
    assert lru.get("4") is None

