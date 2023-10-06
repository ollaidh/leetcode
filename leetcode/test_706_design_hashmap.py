"""
Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

MyHashMap() initializes the object with an empty map.
void put(int key, int value) inserts a (key, value) pair into the HashMap.
If the key already exists in the map, update the corresponding value.
int get(int key) returns the value to which the specified key is mapped,
or -1 if this map contains no mapping for the key.
void remove(key) removes the key and its corresponding value
if the map contains the mapping for the key.
"""


import unittest


class MyHashMap:

    def __init__(self):
        self.buckets: list[tuple[int, int] | None] = [None] * 42
        self.elements = 0
        self.full_threshold = 0.3
        self.is_rehashing = False

    def rehash(self):
        assert not self.is_rehashing
        self.is_rehashing = True
        buckets = self.buckets
        self.buckets = [None] * (2 * len(self.buckets) + 1)
        self.elements = 0
        for b in buckets:
            if b:
                self.put(b[0], b[1])
        self.is_rehashing = False

    def put(self, key: int, value: int) -> None:
        ind = key % len(self.buckets)

        while self.buckets[ind]:
            if self.buckets[ind][0] == key:
                self.buckets[ind] = (key, value)
                return
            else:
                ind = (ind + 1) % len(self.buckets)

        self.buckets[ind] = (key, value)
        self.elements += 1

        if self.elements / len(self.buckets) > self.full_threshold:
            self.rehash()

    def get(self, key: int) -> int:
        ind = key % len(self.buckets)
        while True:
            if not self.buckets[ind]:
                return -1
            if self.buckets[ind][0] == key:
                return self.buckets[ind][1]
            ind = (ind + 1) % len(self.buckets)

    def remove(self, key: int) -> None:
        ind = key % len(self.buckets)
        while True:
            if not self.buckets[ind]:
                return
            if self.buckets[ind][0] == key:
                self.buckets[ind] = None
                self.elements -= 1
                return
            ind = (ind + 1) % len(self.buckets)


class TestMyHashMap(unittest.TestCase):
    def test_hashmap(self):
        hash_map = MyHashMap()
        hash_map.put(1, 11)
        hash_map.put(2, 22)
        hash_map.put(3, 33)
        hash_map.put(1, 12)
        hash_map.put(4, 44)
        self.assertEqual(hash_map.elements, 4)
        self.assertEqual(hash_map.get(3), 33)
        self.assertEqual(hash_map.get(1), 12)

        hash_map.remove(4)
        self.assertEqual(hash_map.elements, 3)
        self.assertEqual(hash_map.get(4), -1)

        hash_map.remove(999)
        self.assertEqual(hash_map.elements, 3)

    def test_rehash(self):
        hash_map = MyHashMap()
        for i in range(1000):
            hash_map.put(i, i)
            self.assertEqual(hash_map.get(i), i)
