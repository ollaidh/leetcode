# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
# Implement the LRUCache class:
# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists.
# Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation,
# evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.


import unittest


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove_node(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def insert_node(self, node):
        prev = self.right.prev
        nxt = self.right
        prev.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove_node(self.cache[key])
            self.insert_node(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove_node(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert_node(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove_node(lru)
            del self.cache[lru.key]


class TestLRUCache(unittest.TestCase):
    def test_LRUCache(self):
        result = []
        lrc = LRUCache(2)
        result.append(lrc.put(1, 1))
        result.append(lrc.put(2, 2))
        result.append(lrc.get(1))
        result.append(lrc.put(3, 3))
        result.append(lrc.get(-1))
        result.append(lrc.put(4, 4))
        result.append(lrc.get(1))
        result.append(lrc.get(3))
        result.append(lrc.get(4))
        self.assertEqual([None, None, 1, None, -1, None, -1, 3, 4], result)


if __name__ == '__main__':
    unittest.main()

